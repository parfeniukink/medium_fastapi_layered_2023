from fastapi import FastAPI
from loguru import logger

from src import presentation
from src.config import settings
from src.infrastructure.application import create as application_factory

# Adjust the logging
# -------------------------------
logger.add(
    "".join(
        [
            str(settings.root_dir),
            "/logs/",
            settings.logging.file.lower(),
            ".log",
        ]
    ),
    format=settings.logging.format,
    rotation=settings.logging.rotation,
    compression=settings.logging.compression,
    level="INFO",
)


# Adjust the application
# -------------------------------
app: FastAPI = application_factory(
    debug=settings.debug,
    rest_routers=(
        presentation.products.rest.router,
        presentation.orders.rest.router,
    ),
    startup_tasks=[],
    shutdown_tasks=[],
    startup_processes=[],
)
