import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import SavingPlansModel
from schemas import SavingPlansSchema, SavingPlansUpdateSchema

blp = Blueprint("Saving plans", __name__, description="List of Saving Plans")

@blp.route("/saving_plans")
class SavingPlans(MethodView):
    @blp.response(200, SavingPlansSchema(many=True))
    def get(self):
        return SavingPlansModel.query.all()
    
    @blp.arguments(SavingPlansSchema)
    @blp.response(201, SavingPlansSchema)
    def post(self, saving_plan_data):
        new_saving_plan = SavingPlansModel(**saving_plan_data)

        try:
            db.session.add(new_saving_plan)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the column")

        return new_saving_plan

   

@blp.route("/saving_plan/<string:saving_plan_id>")
class SavingPlanById(MethodView):
    @blp.arguments(SavingPlansUpdateSchema)
    @blp.response(200, SavingPlansSchema)
    def put(self, saving_plan_data, saving_plan_id):
        saving_plan = SavingPlansModel.query.get_or_404(saving_plan_id)

        if saving_plan:
            saving_plan.target_title = saving_plan_data["target_title"]
            saving_plan.target_amount = saving_plan_data["target_amount"]
            saving_plan.currency_code = saving_plan_data["currency_code"]
            saving_plan.start_date = saving_plan_data["start_date"]
            saving_plan.end_date = saving_plan_data["end_date"]
            saving_plan.starting_capital = saving_plan_data["starting_capital"]
        else:
            abort(404, message="Saving plan with such ID was not found")

        db.session.add(saving_plan)
        db.session.commit()

        return saving_plan

    def delete(self, saving_plan_id):
        saving_plan = SavingPlansModel.query.get_or_404(saving_plan_id)
        
        db.session.delete(saving_plan)
        db.session.commit()

        return {"message": "Saving Plan deleted"}