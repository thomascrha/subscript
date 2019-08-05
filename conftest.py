import sys

sys.path.append(".")

import pytest
from app import create_app, db

from sample_data import add_sample_data, keys as _sample_data


@pytest.fixture
def app():
    return create_app()


@pytest.fixture(scope="session")
def test_client(app):
    return app.test_client()


# create a session fixtures to add the sample data to the db before all
# tests are run 
@pytest.fixture(scope="session")
def sample_data(app):
    return _sample_data


@pytest.fixture(scope="session")
def createdb(app, request):
    db.init_app(app)

    # create schema
    db.drop_all()
    db.create_all()

    # add sample data
    add_sample_data(db)
    db.session.commit()

    def teardown():
        # remove the db 
        db.session.rollback()
        db.session.close()
        db.session.remove()
        db.drop_all()

    # force the teardown when all the tests have been run
    request.addfinalizer(teardown)
    return db


@pytest.fixture(scope="function")
def db(createdb, request):
    def teardown():
        # if a commit error's force a rollback during individual test
        db.session.rollback()

    request.addfinalizer(teardown)
    return db
