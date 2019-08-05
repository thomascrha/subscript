import sys
import pytest
from app import create_app
from app import db as _db

from sample_data import add_sample_data, keys as _sample_data


@pytest.fixture
def app():
    app = create_app("testing")
    ctx = app.app_context()
    ctx.push()
    request.addfinalizer(lambda: ctx.pop())
    return app


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
    _db.init_app(app)

    # create schema
    _db.drop_all()
    _db.create_all()

    # add sample data
    add_sample_data(_db)
    _db.session.commit()

    def teardown():
        # remove the db 
        _db.session.rollback()
        _db.session.close()
        _db.session.remove()
        _db.drop_all()

    # force the teardown when all the tests have been run
    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope="function")
def db(createdb, request):
    def teardown():
        # if a commit error's force a rollback during individual test
        _db.session.rollback()

    request.addfinalizer(teardown)
    return _db
