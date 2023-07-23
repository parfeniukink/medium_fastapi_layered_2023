from src.infrastructure.models import InternalModel

__all__ = ("UserUncommited", "User")


# Internal models
# ------------------------------------------------------
class UserUncommited(InternalModel):
    """This schema is used for creating instance in the database."""

    usernae: str
    password: str


class User(UserUncommited):
    """Existed product representation."""

    id: int
