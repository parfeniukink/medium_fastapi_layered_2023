from pydantic import Field

from src.infrastructure.models import InternalModel, PublicModel

__all__ = ("OrderCreateRequestBody", "OrderPublic", "OrderUncommited", "Order")


# Public models
# ------------------------------------------------------
class _OrderPublic(PublicModel):
    amount: int = Field(description="OpenAPI description")
    product_id: int = Field(description="OpenAPI description")


class OrderCreateRequestBody(_OrderPublic):
    """Order create request body."""

    pass


class OrderPublic(_OrderPublic):
    """The internal application representation."""

    id: int


# Internal models
# ------------------------------------------------------
class _OrderInternal(InternalModel):
    amount: int
    product_id: int
    user_id: int


class OrderUncommited(_OrderInternal):
    """This schema is used for creating instance in the database."""

    pass


class Order(_OrderInternal):
    """Existed order representation."""

    id: int
