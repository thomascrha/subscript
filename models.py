from dateutil.relativedelta import relativedelta
import datetime
from marshmallow import fields

from app import db, ma


# some helper methods for easily adding models to the db
class ModelMixin(object):
    @classmethod
    def create(cls, **kwargs):
        """
        Creates a model.
        """
        return cls(**kwargs)

    @classmethod
    def create_and_add(cls, *args, **kwargs):
        """
        Same as the create method but also adds
        the model to the session.
        """
        model = cls.create(*args, **kwargs)
        db.session.add(model)
        db.session.commit()
        return model


class Plan(ModelMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    site_allowance = db.Column(db.Integer, nullable=False)

    # store buisnes logic on plan as they are all the same
    subscription_time = relativedelta(years=1)

    # simple repr for debugging purposes
    def __repr__(self):
        return '<Plan %r>' % self.name


class PlanSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String()
    price = fields.Float()
    site_allowance = fields.Integer()


plan_schema = PlanSchema()
plans_schema = PlanSchema(many=True)


class Website(ModelMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(80), unique=True, nullable=False)

    # simple repr for debugging purposes
    def __repr__(self):
        return '<Website %r>' % self.url


class WebsiteSchema(ma.Schema):
    id = fields.Integer()
    url = fields.String()


website_schema = WebsiteSchema()
websites_schema = WebsiteSchema(many=True)


class Customer(ModelMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email_address = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    # relationships
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'), nullable=False)
    renewal_date = db.Column(
        db.DateTime,
        default=datetime.datetime.now() + Plan.subscription_time
    )
    websites = db.relationship("CustomerWebsites")

    # simple repr for debugging purposes
    def __repr__(self):
        return '<Customer %r>' % self.username


class CustomerWebsites(ModelMixin, db.Model):
    customer_id = db.Column(
        db.Integer,
        db.ForeignKey('customer.id'),
        primary_key=True
    )
    website_id = db.Column(
        db.Integer,
        db.ForeignKey('website.id'),
        primary_key=True
    )
    website = db.relationship("Website")


class CustomerWebsitesSchema(ma.Schema):
    website = ma.Nested(WebsiteSchema)


class CustomerSchema(ma.Schema):
    id = fields.Integer()
    username = fields.String()
    email_address = fields.String()
    websites = ma.Nested(CustomerWebsitesSchema, many=True)

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
