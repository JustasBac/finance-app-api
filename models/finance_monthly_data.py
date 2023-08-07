from db import db


class FinanceDataModel(db.Model):
    __tablename__ = "finance_data"

    id = db.Column(db.Integer, primary_key=True)
    created_by_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    month = db.Column(db.String(80), unique=True, nullable=False)
    currency_code = db.Column(db.String(5), unique=False, nullable=False)
    income = db.Column(db.Float, unique=False, nullable=True)
    spendings = db.Column(db.Float, unique=False, nullable=True)
    total_balance = db.Column(db.Float, unique=False, nullable=True)