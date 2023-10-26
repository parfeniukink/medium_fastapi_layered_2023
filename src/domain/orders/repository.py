from typing import AsyncGenerator

from sqlalchemy import Result, select
from sqlalchemy.orm import joinedload

from src.infrastructure.application import NotFoundError
from src.infrastructure.database import BaseRepository, OrdersTable

from .aggregates import Order
from .entities import OrderFlat, OrderUncommited

all = ("OrdersRepository",)


class OrdersRepository(BaseRepository[OrdersTable]):
    schema_class = OrdersTable

    async def all(self) -> AsyncGenerator[OrderFlat, None]:
        async for instance in self._all():
            yield OrderFlat.model_validate(instance)

    async def get(self, id_: int) -> Order:
        query = (
            select(OrdersTable)
            .options(
                joinedload(getattr(self.schema_class, "user")),
                joinedload(getattr(self.schema_class, "product")),
            )
            .where(getattr(self.schema_class, "id") == id_)
        )

        result: Result = await self.execute(query)

        if not (instance := result.scalars().one_or_none()):
            raise NotFoundError

        return Order.model_validate(instance)

    async def create(self, schema: OrderUncommited) -> OrderFlat:
        instance: OrdersTable = await self._save(schema.model_dump())
        return OrderFlat.model_validate(instance)
