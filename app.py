from flask import Flask
from flask_smorest import Api

from resources.monthly_savings import blp as MonthlySavinsgBlueprint
from resources.saving_plan import blp as SavingPlansBlueprint

app = Flask(__name__)

app.config['PROPAGATE_EXCEPTIONS'] = True
app.config["API_TITLE"] = "Finance app API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


api = Api(app)

api.register_blueprint(MonthlySavinsgBlueprint)
api.register_blueprint(SavingPlansBlueprint)

# DEV: docker run -p 5000:5000 -w /app -v "$(pwd):/app" finance-api-flask-smorest
# PRODUCTION: docker run -dp 5000:5000 finance-api-flask-smorest
   

