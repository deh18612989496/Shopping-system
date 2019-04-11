
from rest_framework.exceptions import APIException


class PramsException(APIException):
    def __init__(self, err):
        self.detail = err
