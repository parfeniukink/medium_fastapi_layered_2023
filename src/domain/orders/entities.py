from src.infrastructure.application import InternalEntity

__all__ = ("OrderUncommited", "OrderFlat")


class _OrderBase(InternalEntity):
    amount: int
    product_id: int
    user_id: int


class OrderUncommited(_OrderBase):
    """This schema is used for creating instance in the database."""

    pass


class OrderFlat(_OrderBase):
    """Existed order representation."""

    id: int
