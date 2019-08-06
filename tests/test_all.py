import pytest
import json
from tests.sample_data import keys as _sample_data

# resources
from models import (
    Customer,
    CustomerSchema,
    CustomerWebsites,
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

        assert len(data) == expected_length

        # check dicts are serializeable into there respective models
        for model_data in data:
            # the customer model can't intiate with
            # websites so remove if present
            if "websites" in model_data:
                del model_data["websites"]
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

            # the customer model can't intiate with
            # websites so remove if present
            if "websites" in data:
                del data["websites"]
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

        # the customer model can't intiate with
        # websites so remove if present
        if "websites" in data:
            del data["websites"]

        # check response contains model
        model = model_cls(**data)
        # validate data against schema
        schema_cls().load(model)


# customer websites resource tests
class TestCustomerWebsitesResource(object):
    @pytest.mark.parametrize(
        "endpoint, model_id, method, data, fail, expected_status",
        [
            # fail put - plan only allows single website
            (
                "/customers/{}/websites",
                1,
                "put",
                {
                    "websites": [
                        {
                            "url": "www.google.com"
                        }
                    ]
                },
                True,
                None
            ),
            # fail put - website doesn't exist
            (
                "/customers/{}/websites",
                3,
                "put",
                {
                    "websites": [
                        {
                            "url": "www.ajswed.com"
                        }
                    ]
                },
                False,
                STATUS_NOT_FOUND
            ),
            # success put
            (
                "/customers/{}/websites",
                3,
                "put",
                {
                    "websites": [
                        {
                            "url": "www.google.com"
                        }
                    ]
                },
                False,
                STATUS_OK
            ),
            # fail delete - website doesn't exist
            (
                "/customers/{}/websites",
                1,
                "delete",
                {
                    "websites": [
                        {
                            "url": "www.wqenjqw.com"
                        }
                    ]
                },
                True,
                None
            ),
            # success delete
            (
                "/customers/{}/websites",
                3,
                "delete",
                {
                    "websites": [
                        {
                            "url": "www.youtube.com"
                        }
                    ]
                },
                False,
                STATUS_OK
            ),

        ]
    )
    def test_put_delete(
        self,
        db,
        sample_data,
        test_client,
        endpoint,
        method,
        model_id,
        data,
        fail,
        expected_status
    ):
        try:

            if method == "delete":
                response = test_client.delete(
                    endpoint.format(model_id),
                    data=json.dumps(data),
                    content_type="application/json"
                )
            elif method == "put":
                response = test_client.put(
                    endpoint.format(model_id),
                    data=json.dumps(data),
                    content_type="application/json"
                )
            else:
                raise SyntaxError("Invalid method {0}".format(method))

        except ValueError:
            if fail:
                assert True
            else:
                assert False

        if expected_status in (STATUS_OK, STATUS_NOT_FOUND):
            # check for expected status
            assert response.status_code == expected_status, "endpoint did not \
                return expected status: status {0}: expected_status {1}"\
                    .format(response.status_code, expected_status)

            if expected_status == STATUS_OK:
                # make sure its valid json
                data = json.loads(response.data)
                assert data == response.json

                # the customer model can't intiate with
                # websites so remove if present for validation
                if "websites" in data:
                    websites = data["websites"]
                    del data["websites"]

                # check response contains model
                customer = Customer(**data)

                # now add the websites to the created model for validation
                for website in websites:
                    customer_website = CustomerWebsites(
                        website_id=website["website"]["id"],
                        customer_id=data["id"]
                        )

                    if method == "delete":
                        assert customer_website not in customer.websites
                    elif method == "put":
                        customer.websites.append(customer_website)

                # validate data against schema
                CustomerSchema().load(customer)


# customer plan resource tests
class TestCustomerPlanResource(object):
    @pytest.mark.parametrize(
        "endpoint, model_id, data, fail, expected_status",
        [
            # success renew
            (
                "/customers/{}/plan",
                1,
                {
                    "type": "renew",
                    "plan_name": None
                },
                False,
                STATUS_OK
            ),
            # success change
            (
                "/customers/{}/plan",
                1,
                {
                    "type": "change",
                    "plan_name": "plus"
                },
                False,
                STATUS_OK
            ),
            # fail change - same plan
            (
                "/customers/{}/plan",
                1,
                {
                    "type": "change",
                    "plan_name": "single"
                },
                True,
                None
            ),
            # fail change - need to remove some sites to downgrade
            (
                "/customers/{}/plan",
                3,
                {
                    "type": "change",
                    "plan_name": "single"
                },
                True,
                None
            ),
        ]
    )
    def test_put(
        self,
        db,
        sample_data,
        test_client,
        endpoint,
        model_id,
        data,
        fail,
        expected_status
    ):
        try:
            response = test_client.put(
                endpoint.format(model_id),
                data=json.dumps(data),
                content_type="application/json"
            )

        except ValueError:
            if fail:
                assert True
            else:
                assert False

        if expected_status in (STATUS_OK, STATUS_NOT_FOUND):
            # check for expected status
            assert response.status_code == expected_status, "endpoint did not \
                return expected status: status {0}: expected_status {1}"\
                    .format(response.status_code, expected_status)

            # make sure its valid json
            data = json.loads(response.data)
            assert data == response.json

            # the customer model can't intiate with
            # websites so remove if present
            if "websites" in data:
                del data["websites"]

            # check response contains model
            model = Customer(**data)
            # validate data against schema
            CustomerSchema().load(model)
