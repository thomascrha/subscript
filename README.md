# subscript

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


## Decisions

* I'm going to use flask, which technically is a 'framework' - if you could call flask one - I have decided to make this an API
* Make it REST and keep it Zen
* Utilise SQLAlchemy for my models and data
* Utilise pytest instead of pytest

## Setup

```
brew install postgresql
brew service start postgresql 
createdb subscript
createdb subscript-test
env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install -r requirements.txt
```
