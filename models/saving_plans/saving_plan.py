from db import db


class SavingPlansModel(db.Model):
    __tablename__ = "saving_plans"

    id = db.Column(db.Integer, primary_key=True)
    target_title = db.Column(db.String(40), unique=False, nullable=False)
    target_amount = db.Column(db.Float, unique=False, nullable=False)
    currency_code = db.Column(db.String(5), unique=False, nullable=False)
    start_date = db.Column(db.DateTime, unique=False, nullable=False)
    end_date = db.Column(db.DateTime, unique=False, nullable=False)
    starting_capital = db.Column(db.Float, unique=False, nullable=False)
    monthly_savings_list = db.relationship(
        "MonthlySavingsModel", back_populates="saving_plan", cascade="all, delete")
    created_by_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship(
        "UserModel", back_populates="saving_plans")
