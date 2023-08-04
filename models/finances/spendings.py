from db import db


class SpendingsModel(db.Model):
    __tablename__ = "spendings"

    id = db.Column(db.Integer, primary_key=True)
    created_by_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    month = db.Column(db.String(80), unique=True, nullable=False)
    currency_code = db.Column(db.String(5), unique=False, nullable=False)
    value = db.Column(db.Float, unique=False, nullable=False)
