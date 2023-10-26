from src.domain.products import ProductFlat
from src.domain.users import UserFlat

from .entities import OrderFlat

__all__ = ("Order",)


class Order(OrderFlat):
    """This data model aggregates information of an order
    and nested data models from other domains.
    """

    product: ProductFlat
    user: UserFlat
