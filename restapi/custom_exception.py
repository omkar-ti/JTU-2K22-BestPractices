from rest_framework.exceptions import APIException


class UnauthorizedUserException(APIException):
    STATUS_CODE = 404
    DEFAULT_DETAIL = "Not Found"
    DEFAULT_CODE = "Records unavailable"