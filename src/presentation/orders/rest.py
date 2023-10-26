from fastapi import APIRouter, Depends, Request, status

from src.application import orders
from src.application.authentication import get_current_user
from src.domain.orders import Order, OrderFlat
from src.domain.users import UserFlat
from src.infrastructure.application import Response, ResponseMulti

from .contracts import OrderCreateRequestBody, OrderPublic

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.get("", status_code=status.HTTP_200_OK)
async def orders_list(
    request: Request, user: UserFlat = Depends(get_current_user)
) -> ResponseMulti[OrderPublic]:
    """Get all orders."""

    _orders: list[OrderFlat] = await orders.all()
    _orders_public = [OrderPublic.model_validate(order) for order in _orders]

    return ResponseMulti[OrderPublic](result=_orders_public)


@router.post("", status_code=status.HTTP_201_CREATED)
async def order_create(
    request: Request,
    schema: OrderCreateRequestBody,
    user: UserFlat = Depends(get_current_user),
) -> Response[OrderPublic]:
    """Create a new order from huge json, does not matter..."""

    # Save product to the database
    order: Order = await orders.create(payload=schema.dict(), user=user)
    order_public = OrderPublic.model_validate(order)

    return Response[OrderPublic](result=order_public)
