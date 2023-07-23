from typing import AsyncGenerator

from src.infrastructure.database import BaseRepository, OrdersTable

from .models import Order, OrderUncommited

all = ("OrdersRepository",)


class OrdersRepository(BaseRepository[OrdersTable]):
    schema_class = OrdersTable

    async def all(self) -> AsyncGenerator[Order, None]:
        async for instance in self._all():
            yield Order.from_orm(instance)

    async def get(self, id_: int) -> Order:
        instance = await self._get(key="id", value=id_)
        return Order.from_orm(instance)

    async def create(self, schema: OrderUncommited) -> Order:
        instance: OrdersTable = await self._save(schema.dict())
        return Order.from_orm(instance)
