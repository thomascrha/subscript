import models
from flask_restful import Resource
from flask import jsonify, request

from app import db


# default api resources
# Customer list resource
class Customers(Resource):
    def get(self):
        all_customers = models.Customer.query.all()
        result = models.customers_schema.dump(all_customers)
        return jsonify(result.data)

    def post(self):
        # validate data
        data = request.get_json()
        models.CustomerSchema().load(data)

        # add model
        customer = models.Customer.create_and_add(**data)
        return models.customer_schema.jsonify(customer)


# Customer resource
class Customer(Resource):
    def get(self, customer_id):
        # get model
        customer = models.Customer.query.get_or_404(customer_id)

        # serialise model
        return models.customer_schema.jsonify(customer)

    def put(self, customer_id):
        # get model
        customer = models.Customer.query.get_or_404(customer_id)

        data = request.get_json()

        # set values provided
        if "name" in data:
            customer.name = data["name"]

        if "email_address" in data:
            customer.name = data["email_address"]

        if "username" in data:
            customer.name = data["username"]

        # update db with object
        db.session.flush()

        # serialise model
        return models.customer_schema.jsonify(customer)


class CustomerWebsites(Resource):
    # add website(s)
    def put(self, customer_id):
        # check customer exists
        customer = models.Customer.query.get_or_404(customer_id)

        # get data
        data = request.get_json()

        assert "websites" in data

        for website in data["websites"]:
            assert "url" in website

            customer.add_website(website["url"])

        return models.customer_schema.jsonify(customer)

    # remove website(s)
    def delete(self, customer_id):
        # check customer exists
        customer = models.Customer.query.get_or_404(customer_id)

        # get data
        data = request.get_json()

        assert "websites" in data

        for website in data["websites"]:
            assert "url" in website

            customer.remove_website(website["url"])

        return models.customer_schema.jsonify(customer)


class CustomerPlan(Resource):
    def put(self, customer_id):
        # check customer exists
        customer = models.Customer.query.get_or_404(customer_id)

        # get data
        data = request.get_json()

        assert "type" in data
        assert "plan_name" in data

        if data["type"] == "renew":
            customer.renew_plan()
        elif data["type"] == "change":
            customer.change_plan(data["plan_name"])
        else:
            raise ValueError(
                "Unknown Plan action type {0}".format(data["type"])
            )

        return models.customer_schema.jsonify(customer)


# Website list resource
class Websites(Resource):
    def get(self):
        all_websites = models.Website.query.all()
        result = models.websites_schema.dump(all_websites)
        return jsonify(result.data)

    def post(self):
        # validate data
        data = request.get_json()
        models.WebsiteSchema().load(data)

        # add model
        website = models.Website.create_and_add(**data)
        return models.website_schema.jsonify(website)


# Website resource
class Website(Resource):
    def get(self, website_id):
        website = models.Website.query.get_or_404(website_id)
        return models.website_schema.jsonify(website)

    def put(self, website_id):
        # get model
        website = models.Website.query.get_or_404(website_id)

        data = request.get_json()

        # set values provided
        if "url" in data:
            website.url = data["url"]

        # update db with object
        db.session.flush()

        # serialise model
        return models.website_schema.jsonify(website)


# Plan list resource
class Plans(Resource):
    def get(self):
        all_plans = models.Plan.query.all()
        result = models.plans_schema.dump(all_plans)
        return jsonify(result.data)

    def post(self):
        # validate data
        data = request.get_json()
        models.PlanSchema().load(data)

        # add model
        plan = models.Plan.create_and_add(**data)
        return models.plan_schema.jsonify(plan)


# Plan resource
class Plan(Resource):
    def get(self, plan_id):
        plan = models.Plan.query.get_or_404(plan_id)
        return models.plan_schema.jsonify(plan)

    def put(self, plan_id):
        # get model
        plan = models.Plan.query.get_or_404(plan_id)

        data = request.get_json()

        # set values provided
        if "name" in data:
            plan.name = data["name"]

        if "price" in data:
            plan.price = data["price"]

        if "site_allowance" in data:
            plan.site_allowance = data["site_allowance"]

        # update db with object
        db.session.flush()

        # serialise model
        return models.plan_schema.jsonify(plan)
