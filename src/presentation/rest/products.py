from fastapi import APIRouter, Depends, Request, status

from src.application.authentication import get_current_user
from src.domain.products import (
    Product,
    ProductCreateRequestBody,
    ProductPublic,
    ProductRepository,
    ProductUncommited,
)
from src.domain.users import User
from src.infrastructure.database.transaction import transaction
from src.infrastructure.models import Response, ResponseMulti

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("", status_code=status.HTTP_200_OK)
@transaction
async def products_list(request: Request) -> ResponseMulti[ProductPublic]:
    """Get all products."""

    # Get all products from the database
    products_public = [
        ProductPublic.from_orm(product)
        async for product in ProductRepository().all()
    ]

    return ResponseMulti[ProductPublic](result=products_public)


@router.post("", status_code=status.HTTP_201_CREATED)
@transaction
async def product_create(
    _: Request,
    schema: ProductCreateRequestBody,
    user: User = Depends(get_current_user),
) -> Response[ProductPublic]:
    """Create a new product."""

    # Save product to the database
    product: Product = await ProductRepository().create(
        ProductUncommited(**schema.dict())
    )
    product_public = ProductPublic.from_orm(product)

    return Response[ProductPublic](result=product_public)
