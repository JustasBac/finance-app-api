from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request

from db import db
from models import FinanceDataModel
from schemas import FinanceSchema
from sqlalchemy import desc

blp = Blueprint("Finance overview data", __name__,
                description="List of Finance Data by month (income, spendings total-balance)")


@blp.route("/finance_data")
class FinanceData(MethodView):
    @jwt_required()
    @blp.response(200, FinanceSchema(many=True))
    def get(self):
        uid = get_jwt_identity()
        # .order_by(desc(FinanceDataModel.month))
        return FinanceDataModel.query.filter(FinanceDataModel.created_by_id == uid)


@blp.route("/finance_data")
class FinanceOverviewDataByType(MethodView):
    @jwt_required()
    @blp.arguments(FinanceSchema)
    @blp.response(201, FinanceSchema)
    def post(self, finance_data):
        new_finance_month_data_entry = FinanceDataModel(**finance_data)

        uid = get_jwt_identity()

        new_finance_month_data_entry.created_by_id = uid

        try:
            db.session.add(new_finance_month_data_entry)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Data for this month already exists")
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the column")

        return new_finance_month_data_entry


@blp.route("/finance_data/<int:finance_data_entry_id>")
class MonthlySavingsById(MethodView):
    @jwt_required()
    @blp.arguments(FinanceSchema)
    @blp.response(200, FinanceSchema)
    def put(self, finance_data, finance_data_entry_id):
        data_entry = FinanceDataModel.query.get_or_404(finance_data_entry_id)

        uid = get_jwt_identity()

        if data_entry.created_by_id != uid:
            abort(403, message="No permission")

        data_entry.currency_code = finance_data["currency_code"]
        data_entry.income = finance_data["income"]
        data_entry.spendings = finance_data["spendings"]
        data_entry.updated_total_balance = finance_data["updated_total_balance"]

        db.session.add(data_entry)
        db.session.commit()

        return data_entry

    @jwt_required()
    def delete(self, finance_data_entry_id):
        strict_delete = request.args['strict_delete']

        data_entry = FinanceDataModel.query.get_or_404(finance_data_entry_id)

        uid = get_jwt_identity()

        if data_entry.created_by_id != uid:
            abort(403, message="No permission")

        # delete the whole entry
        if strict_delete == "true":
            db.session.delete(data_entry)
            db.session.commit()

            return {"message": "Financial data entry deleted", "ok": True}

        # just delete values of the entry
        data_entry.income = None
        data_entry.spendings = None
        data_entry.updated_total_balance = data_entry.initial_total_balance

        db.session.add(data_entry)
        db.session.commit()

        return {"message": "Financial data values deleted", "ok": True}
