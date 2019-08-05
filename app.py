#!/usr/bin/python3

from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# application set up and db linking
# used for testing suite
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/subscript-test'

    db = SQLAlchemy(app)
    api = Api(app)
    ma = Marshmallow(app)

    from resources import Customer, Customers, Website, Websites, Plan, Plans 

    # api default routes
    api.add_resource(Customers, "/customers", endpoint="customers")
    api.add_resource(Customer, "/customers/<int:customer_id>", endpoint="customer")

    api.add_resource(Websites, "/websites", endpoint="websites")
    api.add_resource(Customer, "/websites/<int:website_id>", endpoint="website")

    api.add_resource(Plans, "/plans", endpoint="plans")

    return app


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/subscript'

db = SQLAlchemy(app)
api = Api(app)
ma = Marshmallow(app)

from resources import Customer, Customers, Website, Websites, Plan, Plans 

# api default routes
api.add_resource(Customers, "/customers", endpoint="customers")
api.add_resource(Customer, "/customers/<int:customer_id>", endpoint="customer")

api.add_resource(Websites, "/websites", endpoint="websites")
api.add_resource(Customer, "/websites/<int:website_id>", endpoint="website")

api.add_resource(Plans, "/plans", endpoint="plans")


if __name__ == "__main__":
    app.run(debug=True)
