import os

from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from db import db
import models

from resources.monthly_savings import blp as MonthlySavinsgBlueprint
from resources.saving_plan import blp as SavingPlansBlueprint
from resources.user import blp as UserBlueprint

def create_app(db_url=None):
    app = Flask(__name__)

    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config["API_TITLE"] = "Finance app API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL","sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
   
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)


    app.config["JWT_SECRET_KEY"] = "144209903379925348535378939497287677465"
    jwt = JWTManager(app)

  

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )


    with app.app_context(): #create all tables
        db.create_all()

    api.register_blueprint(MonthlySavinsgBlueprint)
    api.register_blueprint(SavingPlansBlueprint)
    api.register_blueprint(UserBlueprint)

    return app

# DEV: docker run -p 5000:5000 -w /app -v "$(pwd):/app" finance-app-api
# PRODUCTION: docker run -dp 5000:5000 finance-app-api


   



