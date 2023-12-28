"""
Module which contains pytest fixtures for use in testing the orodha_user_client.
"""
import pytest
from orodha_keycloak import OrodhaCredentials
from tests.fixtures.mock_credentials import MOCK_CREDENTIALS
from tests.fixtures.mock_request_args import MOCK_BULK_RESPONSE_ARGS

@pytest.fixture
def mock_credentials_object():
    credential_object = OrodhaCredentials(**MOCK_CREDENTIALS)
    return credential_object


@pytest.fixture
def mock_post_request(mocker):
    """
    Fixture which patches the requests.post function in order to return fixture data
    from our user service.
    """
    mocker.patch(
        "requests.post",
        return_value=MOCK_BULK_RESPONSE_ARGS,
    )
