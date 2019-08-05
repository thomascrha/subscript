#!/usr/bin/python3

from flask import Flask
from flask_restful import Api, Resource
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# application set up and db linking
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/subscript'

db = SQLAlchemy(app)
api = Api(app)

# default api resources
# Customer list resource
class Customers(Resource):
    def get(self):
        pass

# Customer resource
class Customer(Resource):
    def get(self, customer_id):
        pass
        
    def post(self, customer_id):
        pass
    
    def put(self, customer_id):
        pass

# Website list resource
class Websites(Resource):
    def get(self):
        pass
   
# Website resource
class Website(Resource):
    def get(self, website_id):
        pass
        
    def post(self, website_id):
        pass
    
    def put(self, website_id):
        pass
    
# Plan list resource
class Plans(Resource):
    def get(self):
        pass

# Plan resource
class Plan(Resource):
    def get(self, plan_id):
        pass
        
    def post(self, plan_id):
        pass
    
    def put(self, plan_id):
        pass


# api default routes
api.add_resource(Customers, "/customers", endpoint="customers")
api.add_resource(Customer, "/customers/<int:customer_id>", endpoint="customer")

api.add_resource(Websites, "/websites", endpoint="websites")
api.add_resource(Customer, "/websites/<int:website_id>", endpoint="website")

api.add_resource(Plans, "/plans", endpoint="plans")
api.add_resource(Customer, "/plans/<int:plan_id>", endpoint="plan")


if __name__ == "__main__":
    app.run(debug=True)