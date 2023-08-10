from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required

from db import db
from models import UserModel
from schemas import UserSchema, UserSchemaWithCurrency

blp = Blueprint("Users", __name__, description="List of users")


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(
            UserModel.username == user_data["username"]).first()

        if user and pbkdf2_sha256.verify(user_data['password'], user.password):
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}

        abort(401, message="Invalid credentials")


@blp.route("/refresh")
class TokenRefresh(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user)
        new_refresh_token = create_refresh_token(identity=current_user)

        return {"access_token": new_access_token, "refresh_token": new_refresh_token}


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        new_user = UserModel(
            username=user_data["username"], password=pbkdf2_sha256.hash(user_data["password"]))

        new_user.app_currency_code = "EUR"  # default

        try:
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Such username already exists")

        return {"message": "User successfully created", "ok": True}, 201


@blp.route("/user/<int:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User successfully deleted"}, 200


@blp.route("/app_currency")
class Currency(MethodView):
    @jwt_required()
    @blp.response(200, UserSchemaWithCurrency)
    def get(self):
        uid = get_jwt_identity()

        return UserModel.query.get_or_404(uid)

    @jwt_required()
    @blp.arguments(UserSchemaWithCurrency)
    @blp.response(200, UserSchemaWithCurrency)
    def put(self, currency_data):
        uid = get_jwt_identity()

        user_data = UserModel.query.get_or_404(uid)

        user_data.app_currency_code = currency_data['app_currency_code']

        db.session.add(user_data)
        db.session.commit()

        return user_data
