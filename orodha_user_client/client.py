"""
The main module of the Orodha User Client. Contains UserClient class
which is used to connect to and communicate with the Orodha User Service on behalf
of other Orodha services.
"""
import os
import requests
from orodha_user_client.exceptions import UrlNotFound
from orohda_keycloak import OrodhaCredentials, OrodhakeycloakClient


class OrodhaUserClient:
    """
    The main class for the orodha_user_client package. Allows services to make requests
    to the Orodha User Service progromatically without having to make raw API calls.
    """
    def __init__(self, credentials: OrodhaCredentials):
        self.credentials = credentials
        self.keycloak_client = OrodhakeycloakClient(credentials_object=self.credentials)
        self._set_base_url()

    def _set_base_url(self):
        try:
            self.base_url = os.environ["BASE_USER_URL"]
        except KeyError:
            raise UrlNotFound(message="\"BASE_USER_URL\" must be present in environment")

    def bulk_get(self, request_args: dict):
        """
        Function that calls the user service get-bulk-users route on
        behalf of other services in the Orodha namespace.

        Args:
            request_args(dict): A dictionary of request arguments to be packaged and sent
                to the Orodha user service.
        """
        target_user = request_args.get("target_user")
        if not target_user:
            target_user = self.credentials.client_id

        token_data = self.keycloak_client.exchange_token(target_user=target_user)
        body = {
            "pageSize": request_args.get("pageSize"),
            "pageNum": request_args.get("pageNum"),
            "targets": request_args.get("targets")
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization" : f"Bearer {token_data['access_token']}"
        }
        response = requests.post(self.base_url, data=body, headers=headers)

        return response.json
