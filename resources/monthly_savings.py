from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity

from db import db
from models import MonthlySavingsModel, SavingPlansModel
from schemas import MonthlySavingsSchema, MonthlySavingsUpdateSchema


blp = Blueprint("Monthly savings", __name__,
                description="List of monthly savings that belong to specific Saving Plans")


@blp.route("/monthly_savings")
class MonthlySavings(MethodView):
    @jwt_required()
    @blp.response(200, MonthlySavingsSchema(many=True))
    def get(self):
        return MonthlySavingsModel.query.all()

    @jwt_required()
    @blp.arguments(MonthlySavingsSchema)
    @blp.response(201, MonthlySavingsSchema)
    def post(self, savings_data):
        new_month_savings = MonthlySavingsModel(**savings_data)

        related_saving_plan = SavingPlansModel.query.filter(
            SavingPlansModel.id == savings_data["saving_plan_id"]).first()

        if not related_saving_plan:
            abort(404, message="Such saving plan doesn't exist")

        uid = get_jwt_identity()

        if related_saving_plan.created_by_id != uid:
            abort(403, message="No permission")

        new_month_savings.created_by_id = uid

        try:
            db.session.add(new_month_savings)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Data for this month already exists")
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the column")

        return new_month_savings


@blp.route("/monthly_savings/<int:month_savings_id>")
class MonthlySavingsById(MethodView):
    @jwt_required()
    @blp.arguments(MonthlySavingsUpdateSchema)
    @blp.response(200, MonthlySavingsSchema)
    def put(self, incoming_data, month_savings_id):
        month_savings = MonthlySavingsModel.query.get_or_404(month_savings_id)

        uid = get_jwt_identity()

        if month_savings.created_by_id != uid:
            abort(403, message="No permission")

        month_savings.amount_saved = incoming_data["amount_saved"]

        db.session.add(month_savings)
        db.session.commit()

        return month_savings

    # @jwt_required()
    # def delete(self, month_savings_id):
    #     month_savings = MonthlySavingsModel.query.get_or_404(month_savings_id)

    #     db.session.delete(month_savings)
    #     db.session.commit()

    #     return {"message": "month_savings deleted", "ok": True}
