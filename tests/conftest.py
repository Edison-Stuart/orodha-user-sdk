"""
Module which contains pytest fixtures for use in testing the orodha_user_client.
"""
import pytest
from orodha_keycloak import OrodhaCredentials
from tests.fixtures.mock_credentials import MOCK_CREDENTIALS

@pytest.fixture
def mock_credentials_object():
    credential_object = OrodhaCredentials(**MOCK_CREDENTIALS)
    return credential_object
