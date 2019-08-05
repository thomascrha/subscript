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

    def post(self):
        pass

# Customer resource
class Customer(Resource):
    def get(self, customer_id):
        customer = models.Customer.query.get_or_404(customer_id)
        result = models.customer_schema.dump(customer)
        return jsonify(result.data)

    def put(self, customer_id):
        pass


# Website list resource
class Websites(Resource):
    def get(self):
        all_websites = models.Website.query.all()
        result = models.websites_schema.dump(all_websites)
        return jsonify(result.data)
    
    def post(self):
        pass


# Website resource
class Website(Resource):
    def get(self, website_id):
        website = models.Website.query.get_or_404(website_id)
        result = models.website_schema.dump(website)
        return jsonify(result.data)

    def put(self, website_id):
        pass


# Plan list resource
class Plans(Resource):
    def get(self):
        all_plans = models.Plan.query.all()
        result = models.plans_schema.dump(all_plans)
        return jsonify(result.data)
    
     def post(self):
        pass


# Plan resource
class Plan(Resource):
    def get(self, plan_id):
        plan = models.Plan.query.get_or_404(plan_id)
        result = models.plan_schema.dump(plan)
        return jsonify(result.data)

    def put(self, plan_id):
        pass