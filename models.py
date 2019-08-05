from app import db
from datetime import timedelta


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email_address = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    # simple repr for debugging purposes
    def __repr__(self):
        return '<Customer %r>' % self.username


class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    site_allowance = db.Column(db.Integer, nullable=False)
    # subscription_time = timedelta(years=1) 

    # simple repr for debugging purposes
    def __repr__(self):
        return '<Plan %r>' % self.name


class Website(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(80), unique=True, nullable=False)

    # relationships

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customer = db.relationship('Customer', backref=db.backref('websites', lazy=True))

    # simple repr for debugging purposes
    def __repr__(self):
        return '<Website %r>' % self.url


if __name__ == "__main__":
    db.create_all()