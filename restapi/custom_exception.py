from rest_framework.exceptions import APIException


class UnauthorizedUserException(APIException):
    STATUS_CODE : int = 404
    DEFAULT_DETAIL : str = "Not Found"
    DEFAULT_CODE : str = "Records unavailable"