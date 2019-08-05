import pytest
import json
from tests.sample_data import keys as _sample_data

# resources
from models import (
    Customer,
    CustomerSchema,
    Website,
    WebsiteSchema,
    Plan,
    PlanSchema
)

# status codes
STATUS_OK = 200
STATUS_NOT_FOUND = 404


class TestListResources(object):
    @pytest.mark.parametrize(
        "endpoint, model_cls, expected_length, expected_status",
        [
            ("/customers", Customer, 6, STATUS_OK),
            ("/websites", Website, 9, STATUS_OK),
            ("/plans", Plan, 3, STATUS_OK),
        ]
    )
    def test_get(
        self,
        db,
        sample_data,
        test_client,
        endpoint,
        model_cls,
        expected_length,
        expected_status
    ):
        response = test_client.get(endpoint)

        # check for expected status
        assert response.status_code == expected_status, "endpoint did not \
            return expected status: status {0}: expected_status {1}".format(
                response.status_code, expected_status)

        # make sure its valid json
        data = json.loads(response.data)

        print(data)
        raise
        assert len(data) == expected_length

        # check dicts are serializeable into there respective models
        for model_data in data:
            model_cls(**model_data)

    @pytest.mark.parametrize(
        "endpoint, data, model_cls, schema_cls, expected_status",
        [
            (
                "/customers",
                {
                    "id": 7,
                    "email_address": "test-user-7@subscript.com",
                    "username": "test-user-7",
                    "password": "12345",
                    "plan_id": _sample_data.plan_id_1
                },
                Customer,
                CustomerSchema,
                STATUS_OK
            ),
            (
                "/websites",
                {
                    "id": 10,
                    "url": "www.subscript.com",
                },
                Website,
                WebsiteSchema,
                STATUS_OK
            ),
            (
                "/plans",
                {
                    "id": 4,
                    "name": "super-duper",
                    "price": 350,
                    "site_allowance": 10
                },
                Plan,
                PlanSchema,
                STATUS_OK
            ),
        ]
    )
    def test_post(
        self,
        db,
        sample_data,
        test_client,
        endpoint,
        data,
        model_cls,
        schema_cls,
        expected_status
    ):
        # validate data against schema
        schema_cls().load(data)

        response = test_client.post(
            endpoint,
            data=json.dumps(data),
            content_type="application/json"
        )

        # check for expected status
        assert response.status_code == expected_status, "endpoint did not \
            return expected status: status {0}: expected_status {1}"\
                .format(response.status_code, expected_status)

        # make sure its valid json
        data = json.loads(response.data)
        assert data == response.json

        # check response contains model
        model_cls(**data)


class TestModelResources(object):
    @pytest.mark.parametrize(
        "endpoint, model_cls, model_id, expected_status",
        [
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
        ]
    )
    def test_get(
        self,
        db,
        sample_data,
        test_client,
        endpoint,
        model_cls,
        model_id,
        expected_status
    ):
        response = test_client.get(endpoint.format(model_id))

        # check for expected status
        assert response.status_code == expected_status, "endpoint did not \
            return expected status: status {0}: expected_status {1}".format(
                response.status_code, expected_status)

        if expected_status == STATUS_OK:
            # make sure its valid json
            data = json.loads(response.data)

            model_cls(**data)

    @pytest.mark.parametrize(
        "endpoint, model_cls, schema_cls, model_id, data, expected_status",
        [
            (
                "/customers/{}",
                Customer,
                CustomerSchema,
                1,
                {
                    "username": "fred",
                    "email": "fred@gmail.com",
                    "password": "32345"
                },
                STATUS_OK
            ),
            (
                "/plans/{}",
                Plan,
                PlanSchema,
                1,
                {
                    "price": 23,
                    "site_allowance": 2,
                    "name": "singelton"
                },
                STATUS_OK
            ),
            (
                "/websites/{}",
                Website,
                WebsiteSchema,
                1,
                {
                    "url": "www.google.com.au"
                },
                STATUS_OK
            ),
        ]
    )
    def test_put(
        self,
        db,
        sample_data,
        test_client,
        endpoint,
        model_cls,
        schema_cls,
        model_id,
        data,
        expected_status
    ):
        response = test_client.put(
            endpoint.format(model_id),
            data=json.dumps(data),
            content_type="application/json"
        )

        # check for expected status
        assert response.status_code == expected_status, "endpoint did not \
            return expected status: status {0}: expected_status {1}".format(
                response.status_code, expected_status)

        # make sure its valid json
        data = json.loads(response.data)
        assert data == response.json

        # check response contains model
        model = model_cls(**data)
        # validate data against schema
        schema_cls().load(model)


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
