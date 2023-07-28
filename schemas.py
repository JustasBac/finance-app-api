from marshmallow import Schema, fields

# -----------------------------Monthly Savings
class MonthlySavingsSchema(Schema): # GET, POST, PUT request
    id = fields.Str(dump_only=True)
    month = fields.Str(required=True)
    amount_saved = fields.Float(required=True)
    saving_plan_id = fields.Int(required=True, load_only=True)

class MonthlySavingsUpdateSchema(Schema): # PUT request
    id = fields.Str(required=True)
    amount_saved = fields.Float(required=True)


# -------------------------------Saving Plans
class SavingPlansSchema(Schema): # GET, POST, PUT request
    id = fields.Str(dump_only=True)
    target_title = fields.Str(required=True)
    target_amount = fields.Float(required=True)
    currency_code = fields.Str(required=True)
    start_date = fields.Str(required=True)
    end_date = fields.Str(required=True)
    starting_capital = fields.Float(required=True)
    monthly_savings_list = fields.List(fields.Nested(MonthlySavingsSchema()), dump_only=True)

class SavingPlansUpdateSchema(Schema):  # PUT request
    target_title = fields.Str()
    target_amount = fields.Float()
    currency_code = fields.Str()
    start_date = fields.Str()
    end_date = fields.Str()
    starting_capital = fields.Float()
    