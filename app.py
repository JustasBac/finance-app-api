from flask import Flask, request
from db import saving_plans, monthly_savings
import uuid

app = Flask(__name__)

@app.route("/saving_plans", methods=['GET'])
def get_saving_plans():
    return {"saving_plans": list(saving_plans.values())}

@app.route("/saving_plan", methods=['POST'])
def create_saving_plan():
    saving_plan_data = request.get_json()

    new_saving_plan_id = uuid.uuid4().hex

    new_saving_plan = {**saving_plan_data, "id": new_saving_plan_id}

    saving_plans[new_saving_plan_id] = new_saving_plan

    return new_saving_plan, 201

@app.route("/savings", methods=['POST'])
def add_new_month_savings():
    savings_data = request.get_json()
    
    if savings_data['saving_plan_id'] not in saving_plans:
        return {"message": "Saving plan not found"}, 404
    
    new_savings_id = uuid.uuid4().hex
    new_month_savings = {**savings_data, "id": new_savings_id}
    monthly_savings[new_savings_id] = new_month_savings
        
    return new_month_savings, 201
