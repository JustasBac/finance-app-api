from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    app_currency_code = db.Column(db.String(5), unique=False, nullable=True)
    total_balance = db.Column(db.Float, unique=False, nullable=True)
    saving_plans = db.relationship(
        "SavingPlansModel",  back_populates="user", cascade="all, delete")
    finance_data = db.relationship(
        "FinanceDataModel",  back_populates="user", cascade="all, delete")
