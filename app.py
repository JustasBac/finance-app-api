from flask import Flask, request

app = Flask(__name__)

saving_plans = [
    {
        "target_title": "Apartment",
        "target_amount": 100000,
        "currency_code": 'EUR',
        "start_date": 'xxxx',
        "end_date": 'xxxxxx',
        "savings_per_month": [
            {
                "month": 'June 2023',
                "amount_saved": 500
            }
        ],
        "starting_capital": 80000,
    }
]

@app.route("/saving_plans", methods=['GET'])
def get_saving_plans():
    return {"saving_plans": saving_plans}

@app.route("/saving_plan", methods=['POST'])
def create_saving_plan():
    request_data = request.get_json()

    saving_plans.append(request_data)

    return request_data, 201

@app.route("/saving_plan/<string:target_title>/savings", methods=['POST'])
def add_new_month_savings(target_title):
    request_data = request.get_json()
    
    
    for saving_plan in saving_plans:
        if saving_plan["target_title"] == target_title:
            saving_plan["savings_per_month"].append(request_data)
            return request_data, 201
        
    return {"message": "Saving plan not found"}, 404
