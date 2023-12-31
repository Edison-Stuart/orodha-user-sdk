"""
Module which contains pytest fixtures for use in testing the orodha_user_client.
"""
import pytest
from orodha_keycloak import OrodhaCredentials
from tests.fixtures.mock_credentials import MOCK_CREDENTIALS
from tests.fixtures.mock_request_args import MOCK_TOKEN_EXCHANGE_RESPONSE


class MockOrodhaKeycloakClient:
    """Mock OrodhaKeycloakConnection object to return keycloak fixture functions in testing."""

    def __init__(self, *args, **kwargs):
        self.mock_args = args
        self.mock_kwargs = kwargs

    def exchange_token(self, *args, **kwargs):
        return MOCK_TOKEN_EXCHANGE_RESPONSE

@pytest.fixture
def mock_credentials_object():
    credential_object = OrodhaCredentials(**MOCK_CREDENTIALS)
    return credential_object


@pytest.fixture
def mock_orodha_keycloak(mocker):
    """
    Fixture which patches the OrodhaKeycloakClient class for use in testing
    the user client.
    """
    mocker.patch(
        "orodha_keycloak.OrodhaKeycloakClient",
        return_value=MockOrodhaKeycloakClient(),
    )
