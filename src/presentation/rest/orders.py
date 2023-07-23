from fastapi import APIRouter, Depends, Request, status

from src.application import orders
from src.application.authentication import get_current_user
from src.domain.orders import (
    Order,
    OrderCreateRequestBody,
    OrderPublic,
    OrdersRepository,
)
from src.domain.users import User
from src.infrastructure.database.transaction import transaction
from src.infrastructure.models import Response, ResponseMulti

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.get("", status_code=status.HTTP_200_OK)
@transaction
async def orders_list(
    request: Request, user: User = Depends(get_current_user)
) -> ResponseMulti[OrderPublic]:
    """Get all orders."""

    # Get all products from the database
    orders_public = [
        OrderPublic.from_orm(order) async for order in OrdersRepository().all()
    ]

    return ResponseMulti[OrderPublic](result=orders_public)


@router.post("", status_code=status.HTTP_201_CREATED)
async def order_create(
    request: Request,
    schema: OrderCreateRequestBody,
    user: User = Depends(get_current_user),
) -> Response[OrderPublic]:
    """Create a new order."""

    # Save product to the database
    order: Order = await orders.create(payload=schema.dict(), user=user)
    order_public = OrderPublic.from_orm(order)

    return Response[OrderPublic](result=order_public)
