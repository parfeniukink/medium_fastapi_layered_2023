from contextlib import asynccontextmanager
from typing import AsyncGenerator

from loguru import logger
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.application import DatabaseError

from .session import CTX_SESSION, create_session

__all__ = ("transaction",)


@asynccontextmanager
async def transaction() -> AsyncGenerator[AsyncSession, None]:
    """Use this context manager to perform database transactions. in any coroutine in the source code."""

    session: AsyncSession = create_session()
    CTX_SESSION.set(session)

    try:
        yield session
        await session.commit()
    except DatabaseError as error:
        # NOTE: If any sort of issues are occurred in the code
        #       they are handled on the BaseCRUD level and raised
        #       as a DatabseError.
        #       If the DatabseError is handled within domain/application
        #       levels it is possible that `await session.commit()`
        #       would raise an error.
        logger.error(f"Rolling back changes. {error}")
        await session.rollback()
        raise DatabaseError
    except (IntegrityError, InvalidRequestError) as error:
        # NOTE: Since there is a session commit on this level it should
        #       be handled because it can raise some errors also
        logger.error(f"Rolling back changes.\n{error}")
        await session.rollback()
    finally:
        await session.close()
