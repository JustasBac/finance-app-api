import os

from flask import Flask
from flask_smorest import Api

from db import db
import models

from resources.monthly_savings import blp as MonthlySavinsgBlueprint
from resources.saving_plan import blp as SavingPlansBlueprint

def create_app(db_url=None):
    app = Flask(__name__)

    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config["API_TITLE"] = "Finance app API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL","sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    api = Api(app)

    with app.app_context(): #create all tables
        db.create_all()

    api.register_blueprint(MonthlySavinsgBlueprint)
    api.register_blueprint(SavingPlansBlueprint)

    return app

# DEV: docker run -p 5000:5000 -w /app -v "$(pwd):/app" finance-app-api
# PRODUCTION: docker run -dp 5000:5000 finance-app-api
   



