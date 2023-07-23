from src.domain.orders import Order, OrdersRepository, OrderUncommited
from src.domain.users import User
from src.infrastructure.database.transaction import transaction


@transaction
async def create(payload: dict, user: User) -> Order:
    payload.update(user_id=user.id)

    order = await OrdersRepository().create(OrderUncommited(**payload))

    # Do som other stuff...

    return order
