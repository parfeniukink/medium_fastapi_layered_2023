from pydantic import Field

from src.infrastructure.application import PublicEntity


class TokenClaimRequestBody(PublicEntity):
    login: str = Field("OpenAPI documentation")
    password: str = Field("OpenAPI documentation")


class RefreshAccessTokenRequestBody(PublicEntity):
    refresh: str = Field("OpenAPI documentation")


class TokenClaimPublic(PublicEntity):
    access: str = Field("OpenAPI documentation")
    refresh: str = Field("OpenAPI documentation")
