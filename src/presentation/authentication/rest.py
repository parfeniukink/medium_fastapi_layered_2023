from fastapi import APIRouter, Request, status

from src.infrastructure.application import Response

from .contracts import (
    RefreshAccessTokenRequestBody,
    TokenClaimPublic,
    TokenClaimRequestBody,
)

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/token",
    response_model=Response[TokenClaimPublic],
    status_code=status.HTTP_201_CREATED,
)
async def token_claim(
    request: Request,
    schema: TokenClaimRequestBody,
) -> Response[TokenClaimPublic]:
    """Claim for access and refresh tokens."""

    # 🔗 https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
    raise NotImplementedError


@router.post(
    "/token/refresh",
    response_model=Response[TokenClaimPublic],
    status_code=status.HTTP_201_CREATED,
)
async def token_refresh(
    request: Request,
    schema: RefreshAccessTokenRequestBody,
) -> Response[TokenClaimPublic]:
    """Refresh the access token."""

    # 🔗 https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
    raise NotImplementedError
