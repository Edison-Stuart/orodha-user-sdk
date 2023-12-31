import pytest
import requests_mock
from orodha_user_client import OrodhaUserClient
from tests.fixtures.mock_credentials import MOCK_BASE_URL
from tests.fixtures.mock_request_args import MOCK_BULK_REQUEST_ARGS, MOCK_BULK_RESPONSE_ARGS

def test_bulk_get(mock_credentials_object, mock_orodha_keycloak):
    user_client = OrodhaUserClient(mock_credentials_object, base_url=MOCK_BASE_URL)

    with requests_mock.Mocker() as mock_request:
        mock_request.post(f"{MOCK_BASE_URL}/get-bulk-users", json=MOCK_BULK_RESPONSE_ARGS)

        response = user_client.bulk_get(MOCK_BULK_REQUEST_ARGS)
        assert response == MOCK_BULK_RESPONSE_ARGS
