from typing import AsyncGenerator

from src.infrastructure.database import BaseRepository, UsersTable

from .entities import UserFlat, UserUncommited

all = ("UsersRepository",)


class UsersRepository(BaseRepository[UsersTable]):
    schema_class = UsersTable

    async def all(self) -> AsyncGenerator[UserFlat, None]:
        async for instance in self._all():
            yield UserFlat.model_validate(instance)

    async def get(self, id_: int) -> UserFlat:
        instance = await self._get(key="id", value=id_)
        return UserFlat.model_validate(instance)

    async def create(self, schema: UserUncommited) -> UserFlat:
        instance: UsersTable = await self._save(schema.model_dump())
        return UserFlat.model_validate(instance)
