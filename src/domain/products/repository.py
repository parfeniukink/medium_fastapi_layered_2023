from typing import AsyncGenerator

from src.infrastructure.database import BaseRepository, ProductsTable

from .entities import ProductFlat, ProductUncommited

all = ("ProductRepository",)


class ProductRepository(BaseRepository[ProductsTable]):
    schema_class = ProductsTable

    async def all(self) -> AsyncGenerator[ProductFlat, None]:
        async for instance in self._all():
            yield ProductFlat.from_orm(instance)

    async def get(self, id_: int) -> ProductFlat:
        instance = await self._get(key="id", value=id_)
        return ProductFlat.from_orm(instance)

    async def create(self, schema: ProductUncommited) -> ProductFlat:
        instance: ProductsTable = await self._save(schema.model_dump())
        return ProductFlat.from_orm(instance)
