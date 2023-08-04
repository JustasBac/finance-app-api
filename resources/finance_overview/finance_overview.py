from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity

from db import db
from models import IncomeModel, SpendingsModel, TotalBalanceModel
from schemas import FinanceSchema, FinanceParameterSchema, FinanceParameterUpdateSchema

blp = Blueprint("Finance overview", __name__,
                description="List of Finance Data (income, spendings total-balance)")


FINANCE_DATA_MODELS_BY_TYPE = {
    "income": IncomeModel,
    "spendings": SpendingsModel,
    "total_balance": TotalBalanceModel,
}


@blp.route("/finance_overview_data")
class FinanceData(MethodView):
    @jwt_required()
    @blp.response(200, FinanceSchema)
    def get(self):
        uid = get_jwt_identity()

        return {"total_balance_list": TotalBalanceModel.query.filter(
            TotalBalanceModel.created_by_id == uid),
            "income_list": IncomeModel.query.filter(
            IncomeModel.created_by_id == uid),
            "spendings_list": SpendingsModel.query.filter(
            SpendingsModel.created_by_id == uid)
        }


@blp.route("/finance_overview_data/<string:finance_data_type>")
class FinanceOverviewDataByType(MethodView):
    @jwt_required()
    @blp.arguments(FinanceParameterSchema)
    @blp.response(201, FinanceParameterSchema)
    def post(self, finance_data, finance_data_type):
        if finance_data_type in FINANCE_DATA_MODELS_BY_TYPE:
            finance_data_model = FINANCE_DATA_MODELS_BY_TYPE[finance_data_type]

        new_data_entry = finance_data_model(**finance_data)

        uid = get_jwt_identity()

        new_data_entry.created_by_id = uid

        try:
            db.session.add(new_data_entry)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Data for this month already exists")
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the column")

        return new_data_entry


@blp.route("/finance_overview_data/<string:finance_data_type>/<int:finance_data_entry_id>")
class MonthlySavingsById(MethodView):
    @jwt_required()
    @blp.arguments(FinanceParameterUpdateSchema)
    @blp.response(200, FinanceParameterSchema)
    def put(self, finance_data, finance_data_type, finance_data_entry_id):
        if finance_data_type in FINANCE_DATA_MODELS_BY_TYPE:
            finance_data_model = FINANCE_DATA_MODELS_BY_TYPE[finance_data_type]

        data_entry = finance_data_model.query.get_or_404(finance_data_entry_id)

        uid = get_jwt_identity()

        if data_entry.created_by_id != uid:
            abort(403, message="No permission")

        data_entry.currency_code = finance_data["currency_code"]
        data_entry.value = finance_data["value"]

        db.session.add(data_entry)
        db.session.commit()

        return data_entry
