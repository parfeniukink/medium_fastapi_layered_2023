from src.domain.products import (
    ProductFlat,
    ProductRepository,
    ProductUncommited,
)
from src.infrastructure.database import transaction


async def get_all() -> list[ProductFlat]:
    """Get all products from the database."""

    async with transaction():
        return [product async for product in ProductRepository().all()]


async def create(schema: ProductUncommited) -> ProductFlat:
    """Create a database record for the product."""

    async with transaction():
        return await ProductRepository().create(schema)
