# subscript

## tl;dr

* Used flask, which technically is a 'framework' - if you could call flask one - I have decided to make this an API
* REST and keep it Zen and PEP8
* Utilised SQLAlchemy for my models and data
* Utilised pytest instead of unittest
* Utilised marshmallow for serialization and validation
* Set myself a 24 hour limit - which I kept

### Setup

```
git clone https://github.com/thomascrha/subscript.git
cd subscript

# install postgres
brew install postgresql
brew service start postgresql

# createdb
createdb subscript
createdb subscript-test
env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install -r requirements.txt

./manage db upgrade
```

###### Run:

```
./manage.py runserver
```

###### Tests:

```
./manage.py test
```

### Endopoints

content type = `application/json`

* `/customers` GET
* `/customers/<int:customer_id>` GET POST PUT
    * POST required data (email_address, name, plan_id, password, username)
    * PUT data that can be changed (email_address, name, password, username)
* `/customers/<int:customer_id>/plan` PUT
    * PUT required data (plan_name)
* `/customers/<int:customer_id>/websites` PUT DELETE
    * DELETE required data (website_url)
    * PUT data that can be changed (website_url)
* `/websites` GET
* `/websites/<int:website_id>` GET POST PUT
    * POST required data (url)
    * PUT data that can be changed (url)
* `/plans` GET
* `/plans/<int:customer_id>` GET POST PUT
    * POST required data (name, site_allowance, price)
    * PUT data that can be changed (name, site_allowance, price)


## Brief

Licencing System

We would like to see how you solve an OO design problem. Let's create a simple subscription system. 
The goal is to emulate buying a yearly plan and attach website(s) to it.

There are 3 business entities : 

* Customer - has a name, a password an email address, a subscription and a subscription renewal date. 
- Plan - has a name, a price, and a number of websites allowance. 
- Website - has an URL, and a customer


A customer should be able to subscribe to plan, move from a plan to another and manage websites (add/update/remove) according to his plan.
Subscriptions have a 1-year time value.


Notes : 
- Having a DB is optional
- We have 3 plans :
    - Single, 1 website, 49$
    - Plus, 3 websites $99
    - Infinite, unlimited websites $249
- Please add automated tests, using unittest
- Please use plain Python for this test : no framework . Of course any useful libraries can be used
