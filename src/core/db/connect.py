from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine

from src.core.config.db import settings_db


engine = create_async_engine(settings_db.database_url, echo=settings_db.DB_ECHO_LOG)
