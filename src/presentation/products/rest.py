from fastapi import APIRouter, Depends, Request, status

from src.application import authentication, products
from src.domain.products import (
    ProductFlat,
    ProductRepository,
    ProductUncommited,
)
from src.domain.users import UserFlat
from src.infrastructure.application import Response, ResponseMulti

from .contracts import ProductCreateRequestBody, ProductPublic

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("", status_code=status.HTTP_200_OK)
async def products_list(request: Request) -> ResponseMulti[ProductPublic]:
    """Get all products."""

    _products: list[ProductFlat] = await products.get_all()
    _products_public: list[ProductPublic] = [
        ProductPublic.model_validate(product) for product in _products
    ]

    return ResponseMulti[ProductPublic](result=_products_public)


@router.post("", status_code=status.HTTP_201_CREATED)
async def product_create(
    request: Request,
    schema: ProductCreateRequestBody,
    user: UserFlat = Depends(authentication.get_current_user),
) -> Response[ProductPublic]:
    """Create a new product."""

    _product: ProductFlat = await ProductRepository().create(
        ProductUncommited(**schema.model_dump())
    )
    _product_public = ProductPublic.model_validate(_product)

    return Response[ProductPublic](result=_product_public)
