from typing import AsyncGenerator

from src.domain.products.models import Product, ProductUncommited
from src.infrastructure.database import BaseRepository, ProductsTable

all = ("ProductRepository",)


class ProductRepository(BaseRepository[ProductsTable]):
    schema_class = ProductsTable

    async def all(self) -> AsyncGenerator[Product, None]:
        async for instance in self._all():
            yield Product.from_orm(instance)

    async def get(self, id_: int) -> Product:
        instance = await self._get(key="id", value=id_)
        return Product.from_orm(instance)

    async def create(self, schema: ProductUncommited) -> Product:
        instance: ProductsTable = await self._save(schema.dict())
        return Product.from_orm(instance)
