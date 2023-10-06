from src.infrastructure.application import InternalEntity

__all__ = ("ProductUncommited", "ProductFlat")


# Internal models
# ------------------------------------------------------
class _ProductBase(InternalEntity):
    name: str
    price: int


class ProductUncommited(_ProductBase):
    """This schema is used for creating instance in the database."""

    pass


class ProductFlat(_ProductBase):
    """Database record representation."""

    id: int
