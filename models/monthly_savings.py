from db import db

class MonthlySavingsModel(db.Model):
    __tablename__ = "monthly_savings"

    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String(80), unique=True, nullable=False) # month has to be unique and not null
    amount_saved = db.Column(db.Float, unique=False, nullable=False)
    saving_plan_id = db.Column(db.Integer, db.ForeignKey("saving_plans.id"),unique=False, nullable=False)
    saving_plan = db.relationship("SavingPlansModel", back_populates="monthly_savings_list")