import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import saving_plans, monthly_savings
from schemas import SavingPlansSchema, SavingPlansUpdateSchema

blp = Blueprint("Saving plans", __name__, description="List of Saving Plans")

@blp.route("/saving_plans")
class SavingPlans(MethodView):
    @blp.response(200, SavingPlansSchema(many=True))
    def get(self):
        return saving_plans.values()
    
    @blp.arguments(SavingPlansSchema)
    @blp.response(201, SavingPlansSchema)
    def post(self, saving_plan_data):
        new_saving_plan_id = uuid.uuid4().hex

        new_saving_plan = {**saving_plan_data, "id": new_saving_plan_id}

        saving_plans[new_saving_plan_id] = new_saving_plan

        return new_saving_plan

   

@blp.route("/saving_plan/<string:saving_plan_id>")
class SavingPlanById(MethodView):
    @blp.arguments(SavingPlansUpdateSchema)
    @blp.response(200, SavingPlansSchema)
    def put(self, saving_plan_data, saving_plan_id):
        try:
            saving_plan = saving_plans[saving_plan_id]
            saving_plan |= saving_plan_data
            
            return saving_plan
        except KeyError:
            abort(404, message="Saving plan with such ID is not found")

    def delete(self, saving_plan_id):
        try:
            del saving_plans[saving_plan_id]

            for monthly_saving in monthly_savings.values():
                if monthly_saving["saving_plan_id"] == str(saving_plan_id):
                    monthly_plan_id = monthly_saving['id']
                    del monthly_savings[monthly_plan_id]
                    break

            return {"message": "Saving plan deleted"}
        except KeyError:
            abort(404, message="Saving plan with such ID is not found")