from abc import ABC, abstractmethod
from typing import Optional
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    model = None

    @abstractmethod
    async def all(self):
        raise NotImplementedError

    @abstractmethod
    async def filter(self, **filters):
        raise NotImplementedError

    @abstractmethod
    async def create(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def update(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, pk: Optional[int], **kwargs):
        raise NotImplementedError


class BaseRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, pk: int = None):
        instance = select(self.model).where(self.model.id == pk)
        return await self.session.scalar(instance)

    async def all(self):
        stmt = select(self.model)
        row = await self.session.execute(stmt)
        return row.scalars().all()

    async def filter(self, **filters):
        stmt = select(self.model).filter_by(**filters)
        row = await self.session.execute(stmt)
        return row.scalars().all()

    async def create(self, data):
        instance = self.model(**data)
        print(instance)
        self.session.add(instance)
        return instance

    async def update(self, **kwargs):
        ...

    async def delete(self, pk: Optional[int], **kwargs):
        result = await self.session.execute(delete(self.model).filter_by(id=pk))
        if not result.rowcount():
            pass
