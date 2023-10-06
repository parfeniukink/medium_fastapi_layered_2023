from src.domain.orders import (
    Order,
    OrderFlat,
    OrdersRepository,
    OrderUncommited,
)
from src.domain.users import UserFlat
from src.infrastructure.database import transaction


async def all() -> list[OrderFlat]:
    """Get all orders from the database."""

    async with transaction():
        repository = OrdersRepository()
        orders = [order async for order in repository.all()]

    return orders


async def create(payload: dict, user: UserFlat) -> Order:
    """Create a new order from huge json, does not matter..."""

    payload.update(user_id=user.id)

    async with transaction():
        repository = OrdersRepository()
        order_flat: OrderFlat = await repository.create(
            OrderUncommited(**payload)
        )
        rich_order: Order = await repository.get(order_flat.id)

    # Do som other stuff...

    return rich_order
