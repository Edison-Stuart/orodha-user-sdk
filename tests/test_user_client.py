from orodha_user_client import OrodhaUserClient

def test_bulk_get(mock_credentials_object):
    user_client = OrodhaUserClient(mock_credentials_object)
    
