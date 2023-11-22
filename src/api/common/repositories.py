from abc import ABC, abstractmethod
from typing import Optional


class AbstractRepository(ABC):
    model = None

    @abstractmethod
    async def all(self, **filters):
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
