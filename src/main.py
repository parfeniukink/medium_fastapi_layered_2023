from fastapi import FastAPI
from loguru import logger

from src.config import settings
from src.infrastructure import application
from src.presentation import rest

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
app: FastAPI = application.create(
    debug=settings.debug,
    rest_routers=(rest.products.router, rest.orders.router),
    startup_tasks=[],
    shutdown_tasks=[],
)
