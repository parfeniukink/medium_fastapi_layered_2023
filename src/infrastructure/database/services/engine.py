from functools import lru_cache

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from src.config import settings


@lru_cache(maxsize=1)
def create_engine() -> AsyncEngine:
    """Create a new async database engine.
    A function result is cached since there is not reason to
    initiate the engine more than once since session is created
    for each separate transaction if needed.
    """

    return create_async_engine(
        settings.database.url, future=True, pool_pre_ping=True, echo=False
    )
