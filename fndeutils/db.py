import logging
import os

import asyncpg

logger = logging.getLogger("red.foxy.database")

logger.info("Database module loaded")

_pool: asyncpg.Pool | None = None


async def get_pool() -> asyncpg.Pool:
    logger.debug("Getting database connection pool")
    global _pool
    if _pool is None or _pool._closed:
        logger.info("Creating new database connection pool")
        _pool = await asyncpg.create_pool(
            os.getenv("DATABASE_DSN"),
            min_size=10,
            max_size=15,
        )
        logger.info("Database connection pool created")
    logger.info("Returning database connection pool")
    return _pool
