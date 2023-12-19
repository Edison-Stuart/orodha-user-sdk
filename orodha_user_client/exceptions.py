"""
Module containing custom exceptions for the orodha_user_client package.
"""

class UrlNotFound(Exception):
    """
    Exception that is thrown when a specified URL
    cannot be found in the environment.
    """
    def __init__(self, message: str = "Service url could not be found in environment"):
        self.message = message
        super().__init__(self.message)
