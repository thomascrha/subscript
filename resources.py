import models
from flask_restful import Resource
from flask import jsonify

# default api resources
# Customer list resource
class Customers(Resource):
    def get(self):
        all_customers = models.Customer.query.all()
        result = models.customers_schema.dump(all_customers)
        return jsonify(result.data)


# Customer resource
class Customer(Resource):
    def get(self, customer_id):
        return models.Customer.query.get_or_404(customer_id)

    def post(self, customer_id):
        pass

    def put(self, customer_id):
        pass


# Website list resource
class Websites(Resource):
    def get(self):
        all_websites = models.Website.query.all()
        result = models.websites_schema.dump(all_websites)
        return jsonify(result.data)


# Website resource
class Website(Resource):
    def get(self, website_id):
        return models.Website.query.get_or_404(website_id)

    def post(self, website_id):
        pass

    def put(self, website_id):
        pass


# Plan list resource
class Plans(Resource):
    def get(self):
        all_plans = models.Plan.query.all()
        result = models.plans_schema.dump(all_plans)
        return jsonify(result.data)


# Plan resource
class Plan(Resource):
    def get(self, plan_id):
        return models.Plan.query.get_or_404(plan_id)

    def post(self, plan_id):
        pass

    def put(self, plan_id):
        pass