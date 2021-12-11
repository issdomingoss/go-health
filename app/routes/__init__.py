from flask import Flask
from app.routes.client_blueprint import bp_clients
from app.routes.professional_blueprint import bp_professional,bp_teste
from app.routes.food_plan_blueprint import bp_food_plan


def init_app(app: Flask):
    app.register_blueprint(bp_clients)
    app.register_blueprint(bp_professional)
    app.register_blueprint(bp_food_plan)
    app.register_blueprint(bp_teste)
