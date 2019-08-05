import pytest
import json
from jsoncompare import jsoncompare
from tests.sample_data import keys as _sample_data

# resources
from models import (
    Customer,
    Website,
    Plan,
)

# mime types
MIMETYPE_JSON = "application/json"

# status codes
STATUS_OK = 200
STATUS_BAD_REQUEST = 400
STATUS_NOT_FOUND = 404


class TestListResources(object):
    @pytest.mark.parametrize("endpoint, model_cls, expected_length, expected_status", [
        ("/customers", Customer, 6, STATUS_OK),
        ("/websites", Website, 9, STATUS_OK),
        ("/plans", Plan, 3, STATUS_OK),
    ])
    def test_get(self, db, test_client, endpoint, model_cls, expected_length, expected_status):
        response = test_client.get(endpoint)

        # check for expected status
        assert response.status_code == expected_status, "endpoint did not return expected status: status {0}: expected_status {1}".format(response.status_code, expected_status)

        # make sure its valid json
        data = json.loads(response.data)

        assert len(data) == expected_length

        # check dicts are serializeable into there respective models
        for model_data in data:
            model = model_cls(**model_data)
                    

class TestModelResources(object):
    @pytest.mark.parametrize("endpoint, model_cls, model_id, expected_status", [
        ("/customers/{}", Customer, 1, STATUS_OK),
        ("/customers/{}", Customer, 6, STATUS_OK),
        ("/customers/{}", Customer, 100, STATUS_NOT_FOUND),
        ("/plans/{}", Plan, 1, STATUS_OK),
        ("/plans/{}", Plan, 2, STATUS_OK),
        ("/plans/{}", Plan, 3, STATUS_OK),
        ("/plans/{}", Plan, 100, STATUS_NOT_FOUND),
        ("/websites/{}", Website, 1, STATUS_OK),
        ("/websites/{}", Website, 9, STATUS_OK),
        ("/websites/{}", Website, 100, STATUS_NOT_FOUND),
    ])
    def test_get(self, db, test_client, sample_data, endpoint, model_cls, model_id, expected_status):
        response = test_client.get(endpoint.format(model_id))

        # check for expected status
        assert response.status_code == expected_status, "endpoint did not return expected status: status {0}: expected_status {1}".format(response.status_code, expected_status)

        if expected_status == STATUS_OK: 
            # make sure its valid json
            data = json.loads(response.data)

            model_cls(**data)


    def test_post(self):
        pass

    def test_put(self):
        pass


# customer tests
class TestCustomerModel(object):
    def test(self):
        pass


# website tests
class TestWebsiteModel(object):
    def test(self):
        pass


# plan tests
class TestPlanModel(object):
    def test(self):
        pass
