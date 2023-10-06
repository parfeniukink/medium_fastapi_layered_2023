from pydantic import Field

from src.infrastructure.application import PublicEntity


class _OrderBase(PublicEntity):
    amount: int = Field(description="OpenAPI description")
    product_id: int = Field(description="OpenAPI description")


class OrderCreateRequestBody(_OrderBase):
    """Order create request body."""

    pass


class OrderPublic(_OrderBase):
    """The internal application representation."""

    id: int
