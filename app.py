#!/usr/bin/python3

from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


# application set up and db linking
# used for testing suite
def create_app(config=None):
    app = Flask(__name__)
    if config == "testing":
        app.config[
            "SQLALCHEMY_DATABASE_URI"
        ] = "postgresql://localhost/subscript-test"
        app.config["TESTING"] = True
    else:
        app.config[
            "SQLALCHEMY_DATABASE_URI"
        ] = "postgresql://localhost/subscript"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    api = Api(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    from resources import (
        Customer,
        Customers,
        CustomerWebsites,
        CustomerPlan,
        Website,
        Websites,
        Plan,
        Plans
    )

    # api default routes
    # customer
    api.add_resource(
        Customers,
        "/customers",
        endpoint="customers"
    )
    api.add_resource(
        Customer,
        "/customers/<int:customer_id>",
        endpoint="customer"
    )
    api.add_resource(
        CustomerWebsites,
        "/customers/<int:customer_id>/websites",
        endpoint="customer_websites"
    )
    api.add_resource(
        CustomerPlan,
        "/customers/<int:customer_id>/plan",
        endpoint="customer_plan"
    )

    # website
    api.add_resource(
        Websites,
        "/websites",
        endpoint="websites"
    )
    api.add_resource(
        Website,
        "/websites/<int:website_id>",
        endpoint="website"
    )

    # plan
    api.add_resource(
        Plans,
        "/plans",
        endpoint="plans"
    )
    api.add_resource(
        Plan,
        "/plans/<int:plan_id>",
        endpoint="plan"
    )

    return app
