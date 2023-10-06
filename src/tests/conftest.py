import pytest
from alembic import command as alembic_command
from alembic import config as _alembic_config
from loguru import logger

from src.infrastructure.database import CTX_SESSION

alembic_config = _alembic_config.Config("alembic.ini")


def pytest_configure():
    # Disable logs
    alembic_config.set_section_option("logger_alembic", "level", "ERROR")
    logger.disable("src.infrastructure")
    logger.disable("src.presentation")
    logger.disable("src.domain")
    logger.disable("src.application")


# =====================================================================
# Database specific fixtures and mocks
# =====================================================================
@pytest.fixture(autouse=True)
def auto_prune_database():
    """This fixture automatically cleans the database with alembic
    for each test separately.
    """

    alembic_command.upgrade(alembic_config, "head")
    yield
    alembic_command.downgrade(alembic_config, "base")


@pytest.fixture(autouse=True)
async def _auto_close_session():
    """Autoclose each session after each test.
    NOTE: we'd like to be sure that the session is closed in any case.
    """

    yield
    session = CTX_SESSION.get()
    await session.close()


# =====================================================================
# Application specific fixtures
# =====================================================================
