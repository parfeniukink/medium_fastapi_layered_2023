from typing import TypeVar

from sqlalchemy import Column, ForeignKey, Integer, MetaData, String
from sqlalchemy.orm import Mapped, declarative_base, relationship

__all__ = ("Base", "UsersTable", "ProductsTable", "OrdersTable")

meta = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)


class _Base:
    """Base class for all database models."""

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=_Base, metadata=meta)

ConcreteTable = TypeVar("ConcreteTable", bound=Base)


class UsersTable(Base):
    __tablename__ = "users"

    username: str = Column(String, nullable=False)
    password: str = Column(String, nullable=False)


class ProductsTable(Base):
    __tablename__ = "products"

    name: str = Column(String, nullable=False)
    price: int = Column(Integer, nullable=False)


class OrdersTable(Base):
    __tablename__ = "orders"

    amount: int = Column(Integer, nullable=False, default=1)

    product_id: int = Column(ForeignKey(ProductsTable.id), nullable=False)
    user_id: int = Column(ForeignKey(UsersTable.id), nullable=False)

    user: "Mapped[UsersTable]" = relationship("UsersTable", uselist=False)
    product: "Mapped[ProductsTable]" = relationship(
        "ProductsTable", uselist=False
    )
