from src.infrastructure.application import InternalEntity

__all__ = (
    "TokenPayload",
    "AccessToken",
    "RefreshToken",
)


class TokenPayload(InternalEntity):
    sub: int
    exp: int


class AccessToken(InternalEntity):
    payload: TokenPayload
    raw: str


class RefreshToken(InternalEntity):
    payload: TokenPayload
    raw: str
