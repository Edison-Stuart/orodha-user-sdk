from orodha_user_client import OrodhaUserClient
from tests.fixtures.mock_credentials import MOCK_BASE_URL
from tests.fixtures.mock_request_args import MOCK_BULK_REQUEST_ARGS

def test_bulk_get(mock_credentials_object, mock_post_request):
    user_client = OrodhaUserClient(mock_credentials_object, base_url=MOCK_BASE_URL)
    response = user_client.bulk_get(MOCK_BULK_REQUEST_ARGS)
    
