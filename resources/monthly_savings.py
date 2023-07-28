import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import MonthlySavingsModel
from schemas import MonthlySavingsSchema, MonthlySavingsUpdateSchema


blp = Blueprint("Monthly savings", __name__, description="List of monthly savings that belong to specific Saving Plans")

@blp.route("/monthly_savings")
class MonthlySavings(MethodView):
    @blp.response(200, MonthlySavingsSchema(many=True))
    def get(self):
        return MonthlySavingsModel.query.all()


    @blp.arguments(MonthlySavingsSchema)
    @blp.response(201, MonthlySavingsSchema)
    def post(self, savings_data):
        new_month_savings = MonthlySavingsModel(**savings_data)

        try:
            db.session.add(new_month_savings)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Data for this month already exists")
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the column")

        return new_month_savings

    

@blp.route("/monthly_savings/<string:month_savings_id>")
class MonthlySavingsById(MethodView):
    @blp.arguments(MonthlySavingsUpdateSchema)
    @blp.response(200, MonthlySavingsSchema)
    def put(self, savings_data, month_savings_id):
        month_savings = MonthlySavingsModel.query.get_or_404(month_savings_id)
        raise NotImplementedError("not implemneted yet")