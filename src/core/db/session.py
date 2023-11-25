from typing import Generator

from sqlalchemy.exc import DBAPIError
from sqlalchemy.ext.asyncio import async_sessionmaker
from src.core.db.connect import engine


Session = async_sessionmaker(bind=engine)


async def _get_session() -> Generator[Session, None, None]:
    """Генератор получения сессии БД."""
    session = Session()
    try:
        yield session
        await session.commit()
    except Exception as e:
        await session.rollback()
        raise Exception(str(e))
    finally:
        await session.close()
