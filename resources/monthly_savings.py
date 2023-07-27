import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import saving_plans, monthly_savings
from schemas import MonthlySavingsSchema, MonthlySavingsUpdateSchema

blp = Blueprint("Monthly savings", __name__, description="List of monthly savings that belong to specific Saving Plans")

@blp.route("/monthly_savings")
class MonthlySavings(MethodView):
    @blp.response(200, MonthlySavingsSchema(many=True))
    def get(self):
        return monthly_savings.values()

    @blp.arguments(MonthlySavingsSchema)
    @blp.response(201, MonthlySavingsSchema)
    def post(self, savings_data):
        for monthly_saving in monthly_savings.values():
            if (savings_data["saving_plan_id"] == monthly_saving["saving_plan_id"] and savings_data["month"] == monthly_saving["month"]):
                abort(400, message="Data for this month already exists")

        if savings_data['saving_plan_id'] not in saving_plans:
            abort(404, message="Saving plan not found")
        
        new_savings_id = uuid.uuid4().hex
        new_month_savings = {**savings_data, "id": new_savings_id}
        monthly_savings[new_savings_id] = new_month_savings
            
        return new_month_savings

    

@blp.route("/monthly_savings/<string:month_savings_id>")
class MonthlySavingsById(MethodView):
    @blp.arguments(MonthlySavingsUpdateSchema)
    @blp.response(200, MonthlySavingsSchema)
    def put(self, savings_data, month_savings_id):
        print(month_savings_id)
        print(savings_data)
        try:
            monthly_savings[month_savings_id]['amount_saved'] = savings_data['amount_saved']

            return monthly_savings[month_savings_id]
        except KeyError:
            abort(404, message="Savings data for this month not found")