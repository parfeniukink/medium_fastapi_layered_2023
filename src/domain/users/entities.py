from src.infrastructure.application import InternalEntity

__all__ = ("UserUncommited", "UserFlat")


class UserUncommited(InternalEntity):
    """This schema is used for creating instance in the database."""

    username: str
    password: str


class UserFlat(UserUncommited):
    """Existed product representation."""

    id: int
