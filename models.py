from app import db 
from dateutil.relativedelta import relativedelta


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
        db.session.flush()
        return model


class Customer(ModelMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email_address = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    # relationships
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'), nullable=False)

    # simple repr for debugging purposes
    def __repr__(self):
        return '<Customer %r>' % self.username


class Plan(ModelMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    site_allowance = db.Column(db.Integer, nullable=False)
    subscription_time = relativedelta(years=1)

    # simple repr for debugging purposes
    def __repr__(self):
        return '<Plan %r>' % self.name


class Website(ModelMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(80), unique=True, nullable=False)

    # simple repr for debugging purposes
    def __repr__(self):
        return '<Website %r>' % self.url
