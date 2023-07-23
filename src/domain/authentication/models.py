from pydantic import Field

from src.infrastructure.models import InternalModel, PublicModel

__all__ = (
    "TokenClaimRequestBody",
    "TokenClaimPublic",
    "TokenPayload",
    "AccessToken",
    "RefreshToken",
)


# Public models
# ------------------------------------------------------
class TokenClaimRequestBody(PublicModel):
    login: str = Field("OpenAPI documentation")
    password: str = Field("OpenAPI documentation")


class TokenClaimPublic(PublicModel):
    access: str = Field("OpenAPI documentation")
    refresh: str = Field("OpenAPI documentation")


# Internal models
# ------------------------------------------------------
class TokenPayload(InternalModel):
    sub: int
    exp: int


class AccessToken(InternalModel):
    payload: TokenPayload
    raw_token: str


class RefreshToken(InternalModel):
    payload: TokenPayload
    raw_token: str
