"""
This module is responsible for describing internal application errors.
"""


from typing import Any

from starlette import status

__all__ = (
    "BaseError",
    "BadRequestError",
    "UnprocessableError",
    "NotFoundError",
    "AuthenticationError",
    "AuthorizationError",
    "DatabaseError",
    "ProcessError",
)


class BaseError(Exception):
    def __init__(
        self,
        *_: tuple[Any],
        message: str = "",
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
    ) -> None:
        """The base class for all errors."""

        self.message: str = message
        self.status_code: int = status_code

        super().__init__(message)


class BadRequestError(BaseError):
    """Consider cases when the server can not perform the operation due
    wrong request from the user.
    """

    def __init__(self, *_: tuple[Any], message: str = "Bad request") -> None:
        super().__init__(
            message=message, status_code=status.HTTP_400_BAD_REQUEST
        )


class UnprocessableError(BaseError):
    def __init__(
        self, *_: tuple[Any], message: str = "Validation error"
    ) -> None:
        """Consider cases when the server can not perform the operation due
        any sorts of conditions.
        """

        super().__init__(
            message=message, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )


class NotFoundError(BaseError):
    """Consider cases when the resourse can't be found for this operation."""

    def __init__(self, *_: tuple[Any], message: str = "Not found") -> None:
        super().__init__(
            message=message, status_code=status.HTTP_404_NOT_FOUND
        )


class AuthenticationError(BaseError):
    def __init__(
        self, *_: tuple[Any], message: str = "Authentication error"
    ) -> None:
        """Consider any case the user wants to perform an action
        but correct credentials were not provided.
        """

        super().__init__(
            message=message,
            status_code=status.HTTP_401_UNAUTHORIZED,
        )


class AuthorizationError(BaseError):
    def __init__(
        self, *_: tuple[Any], message: str = "Authorization error"
    ) -> None:
        """Except of the regular authentication error, this one considers
        the case when the user is authenticated but has no permission
        to perform the action, etc...
        """

        super().__init__(
            message=message, status_code=status.HTTP_403_FORBIDDEN
        )


class DatabaseError(BaseError):
    def __init__(
        self, *_: tuple[Any], message: str = "Database error"
    ) -> None:
        """Any internally defined database error
        have to raise this exception.
        """

        super().__init__(
            message=message, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


class ProcessError(BaseError):
    def __init__(
        self, *_: tuple[Any], message: str = "Background process error"
    ) -> None:
        """The error that should be raised by the background process."""

        super().__init__(
            message=message, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
