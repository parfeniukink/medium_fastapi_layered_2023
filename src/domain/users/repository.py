from typing import AsyncGenerator

from src.infrastructure.database import BaseRepository, UsersTable

from .models import User, UserUncommited

all = ("UsersRepository",)


class UsersRepository(BaseRepository[UsersTable]):
    schema_class = UsersTable

    async def all(self) -> AsyncGenerator[User, None]:
        async for instance in self._all():
            yield User.from_orm(instance)

    async def get(self, id_: int) -> User:
        instance = await self._get(key="id", value=id_)
        return User.from_orm(instance)

    async def create(self, schema: UserUncommited) -> User:
        instance: UsersTable = await self._save(schema.dict())
        return User.from_orm(instance)
