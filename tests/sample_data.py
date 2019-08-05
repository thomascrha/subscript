from models import (
    Customer,
    CustomerWebsites,
    Website,
    Plan
)


class keys(object):

    # plan_ids - necessary for params in pytest
    plan_id_1 = 1
    plan_id_2 = 2
    plan_id_3 = 3

    # dynamic data
    data = {}

    @classmethod
    def add(cls, key, value):
        assert key not in cls.data
        cls.data[key] = value

    @classmethod
    def get(cls, key):
        if key not in cls.data:
            raise ValueError("unknown data key: {0}".format(key))

        return cls.data[key]


def add_sample_data(db):
    add_plans(db)
    add_websites(db)
    add_customers(db)


def add_websites(db):
    website_1 = Website.create_and_add(
        id=1,
        url="www.google.com"
    )

    website_2 = Website.create_and_add(
        id=2,
        url="www.ebay.com"
    )

    website_3 = Website.create_and_add(
        id=3,
        url="www.amazon.com"
    )

    website_4 = Website.create_and_add(
        id=4,
        url="www.github.com"
    )

    website_5 = Website.create_and_add(
        id=5,
        url="www.reddit.com"
    )

    website_6 = Website.create_and_add(
        id=6,
        url="www.facebook.com"
    )

    website_7 = Website.create_and_add(
        id=7,
        url="www.twitter.com"
    )

    website_8 = Website.create_and_add(
        id=8,
        url="www.bing.com"
    )

    website_9 = Website.create_and_add(
        id=9,
        url="www.youtube.com"
    )

    keys.add("website_1_id", website_1.id)
    keys.add("website_2_id", website_2.id)
    keys.add("website_3_id", website_3.id)
    keys.add("website_4_id", website_4.id)
    keys.add("website_5_id", website_5.id)
    keys.add("website_6_id", website_6.id)
    keys.add("website_7_id", website_7.id)
    keys.add("website_8_id", website_8.id)
    keys.add("website_9_id", website_9.id)


def add_plans(db):

    # Single, 1 website, $49
    plan_1 = Plan.create_and_add(
        id=keys.plan_id_1,
        name="single",
        price=49,
        site_allowance=1,
    )

    # Plus, 3 websites $99
    plan_2 = Plan.create_and_add(
        id=keys.plan_id_2,
        name="plus",
        price=99,
        site_allowance=3,
    )

    # Infinite, unlimited websites $249
    plan_3 = Plan.create_and_add(
        id=keys.plan_id_3,
        name="infinite",
        price=249,
        site_allowance=0,
    )

    keys.add("plan_1_id", plan_1.id)
    keys.add("plan_2_id", plan_2.id)
    keys.add("plan_3_id", plan_3.id)


def add_customers(db):
    # customer 1
    customer_1 = Customer.create_and_add(
        id=1,
        username="test-user-1",
        email_address="test-user-1@subscript.com",
        password="12345",
        plan_id=keys.get("plan_1_id"),
    )
    customer_1_website_1 = CustomerWebsites.create_and_add(
        website_id=keys.get("website_1_id"),
        customer_id=customer_1.id
    )
    customer_1.websites.append(customer_1_website_1)
    db.session.flush()

    # customer 2
    customer_2 = Customer.create_and_add(
        id=2,
        username="test-user-2",
        email_address="test-user-2@subscript.com",
        password="12345",
        plan_id=keys.get("plan_2_id")
    )
    customer_2_website_1 = CustomerWebsites.create_and_add(
        website_id=keys.get("website_1_id"),
        customer_id=customer_2.id
    )
    customer_2_website_2 = CustomerWebsites.create_and_add(
        website_id=keys.get("website_4_id"),
        customer_id=customer_2.id
    )
    customer_2_website_3 = CustomerWebsites.create_and_add(
        website_id=keys.get("website_9_id"),
        customer_id=customer_2.id
    )
    customer_2.websites += [
        customer_2_website_1,
        customer_2_website_2,
        customer_2_website_3
    ]
    db.session.flush()

    # customer 3
    customer_3 = Customer.create_and_add(
        id=3,
        username="test-user-3",
        email_address="test-user-3@subscript.com",
        password="12345",
        plan_id=keys.get("plan_3_id")
    )
    customer_3_website_1 = CustomerWebsites.create_and_add(
        website_id=keys.get("website_6_id"),
        customer_id=customer_3.id
    )
    customer_3_website_2 = CustomerWebsites.create_and_add(
        website_id=keys.get("website_9_id"),
        customer_id=customer_3.id
    )
    customer_3_website_3 = CustomerWebsites.create_and_add(
        website_id=keys.get("website_7_id"),
        customer_id=customer_3.id
    )
    customer_3_website_4 = CustomerWebsites.create_and_add(
        website_id=keys.get("website_4_id"),
        customer_id=customer_3.id
    )
    customer_3_website_5 = CustomerWebsites.create_and_add(
        website_id=keys.get("website_2_id"),
        customer_id=customer_3.id
    )
    customer_3_website_6 = CustomerWebsites.create_and_add(
        website_id=keys.get("website_3_id"),
        customer_id=customer_3.id
    )
    customer_3.websites += [
        customer_3_website_1,
        customer_3_website_2,
        customer_3_website_3,
        customer_3_website_4,
        customer_3_website_5,
        customer_3_website_6,
    ]
    db.session.flush()

    # customer 4 - no websites
    customer_4 = Customer.create_and_add(
        id=4,
        username="test-user-4",
        email_address="test-user-4@subscript.com",
        password="12345",
        plan_id=keys.get("plan_1_id")
    )

    # customer 5 - 1 remaining site
    customer_5 = Customer.create_and_add(
        id=5,
        username="test-user-5",
        email_address="test-user-5@subscript.com",
        password="12345",
        plan_id=keys.get("plan_2_id")
    )
    customer_5_website_1 = CustomerWebsites.create_and_add(
        website_id=keys.get("website_3_id"),
        customer_id=customer_5.id
    )
    customer_5_website_2 = CustomerWebsites.create_and_add(
        website_id=keys.get("website_7_id"),
        customer_id=customer_5.id
    )
    customer_2.websites += [
        customer_5_website_1,
        customer_5_website_2
    ]
    db.session.flush()

    # customer 6
    customer_6 = Customer.create_and_add(
        id=6,
        username="test-user-6",
        email_address="test-user-6@subscript.com",
        password="12345",
        plan_id=keys.get("plan_3_id")
    )
    customer_6_website_1 = CustomerWebsites.create_and_add(
        website_id=keys.get("website_6_id"),
        customer_id=customer_6.id
    )
    customer_6_website_2 = CustomerWebsites.create_and_add(
        website_id=keys.get("website_9_id"),
        customer_id=customer_6.id
    )
    customer_6_website_3 = CustomerWebsites.create_and_add(
        website_id=keys.get("website_7_id"),
        customer_id=customer_6.id
    )
    customer_6_website_4 = CustomerWebsites.create_and_add(
        website_id=keys.get("website_4_id"),
        customer_id=customer_6.id
    )
    customer_6_website_5 = CustomerWebsites.create_and_add(
        website_id=keys.get("website_2_id"),
        customer_id=customer_6.id
    )
    customer_6_website_6 = CustomerWebsites.create_and_add(
        website_id=keys.get("website_3_id"),
        customer_id=customer_6.id
    )
    customer_6.websites += [
        customer_6_website_1,
        customer_6_website_2,
        customer_6_website_3,
        customer_6_website_4,
        customer_6_website_5,
        customer_6_website_6,
    ]
    db.session.flush()

    keys.add("customer_1_id", customer_1.id)
    keys.add("customer_2_id", customer_2.id)
    keys.add("customer_3_id", customer_3.id)
    keys.add("customer_4_id", customer_4.id)
    keys.add("customer_5_id", customer_5.id)
    keys.add("customer_6_id", customer_6.id)
