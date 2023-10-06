"""
This namespace includes any sorts of factories:
    * data models
    * services factories
    * etc.
"""


from polyfactory.factories.pydantic_factory import ModelFactory

from src.infrastructure.database import transaction

from ..entities import UserFlat, UserUncommited
from ..repository import UsersRepository


class UserUncommitedFactory(ModelFactory[UserUncommited]):
    """This class implements the factory for the UserFlat model."""

    __model__ = UserUncommited


async def create_user(**payload) -> UserFlat:
    """Create a new user in the database."""

    async with transaction():
        return await UsersRepository().create(
            schema=UserUncommitedFactory.build(**payload)
        )
