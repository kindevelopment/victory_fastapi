from typing import Callable
from fastapi import Depends
from src.api.common.repositories import BaseRepository
from src.core.db.session import Session, _get_session


def get_repository(repo_type: BaseRepository) -> Callable[[Session], BaseRepository]:
    def _get_repo(session: Session = Depends(_get_session)):
        """Инициализирует класс репозитория."""
        return repo_type(session)

    return _get_repo
