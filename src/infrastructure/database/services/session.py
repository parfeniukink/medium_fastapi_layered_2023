from contextvars import ContextVar

from sqlalchemy.engine import ResultProxy
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from src.infrastructure.application import DatabaseError

from .engine import create_engine

__all__ = ("create_session", "CTX_SESSION")


def create_session(engine: AsyncEngine | None = None) -> AsyncSession:
    """Creates a new async session to execute SQL queries."""

    return AsyncSession(
        engine or create_engine(), expire_on_commit=False, autoflush=False
    )


CTX_SESSION: ContextVar[AsyncSession] = ContextVar(
    "session", default=create_session()
)


class Session:
    """The basic class to perfoem database operations within the session."""

    # All sqlalchemy errors that can be raised
    _ERRORS = (IntegrityError, InvalidRequestError)

    def __init__(self) -> None:
        self._session: AsyncSession = CTX_SESSION.get()

    async def execute(self, query) -> ResultProxy:
        try:
            result = await self._session.execute(query)
            return result
        except self._ERRORS:
            raise DatabaseError
