import pytest
from tests.sample_data import keys as _sample_data

# resources
from app import (
    Customer,
    Customers,
    Website,
    Websites,
    Plan,
    Plans
)

# mime types
MIMETYPE_JSON = "application/json"

# status codes
STATUS_OK = 200
STATUS_BAD_REQUEST = 400
STATUS_NOT_FOUND = 404


# customer tests
class TestCustomerModel(object):
    def test(self):
        pass


class TestCustomerListResource(object):
    @pytest.mark.parametrize("customer_number, expected_status", [
        (10, STATUS_OK),
    ])
    def test_get(self, db, test_client, sample_data, customer_number, expected_status):
        customers = Customers.get()

        assert customers.status_code == expected_status 
        assert len(customers) == customer_number


class TestCustomerModelResource(object):
    def test_get(self):
        pass

    def test_post(self):
        pass

    def test_put(self):
        pass


# website tests
class TestWebsiteModel(object):
    def test(self):
        pass


class TestWebsiteListResource(object):
    def test_get(self):
        pass


class TestWebsiteModelResource(object):
    def test_get(self):
        pass

    def test_post(self):
        pass

    def test_put(self):
        pass


# plan tests
class TestPlanModel(object):
    def test(self):
        pass


class TestPlanListResource(object):
    def test_get(self):
        pass


class TestPlanModelResource(object):
    def test_get(self):
        pass

    def test_post(self):
        pass

    def test_put(self):
        pass
