from db import db


class FinanceDataModel(db.Model):
    __tablename__ = "finance_data"

    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String(80), unique=False, nullable=False)
    currency_code = db.Column(db.String(5), unique=False, nullable=False)
    income = db.Column(db.Float, unique=False, nullable=True)
    spendings = db.Column(db.Float, unique=False, nullable=True)
    initial_total_balance = db.Column(
        db.Float, unique=False, nullable=True)
    updated_total_balance = db.Column(db.Float, unique=False, nullable=True)
    created_by_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship(
        "UserModel", back_populates="finance_data")
