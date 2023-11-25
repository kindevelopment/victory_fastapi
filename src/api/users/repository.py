from src.api.users.models import Withdraw_types
from src.api.common.repositories import BaseRepository


class UserRepository(BaseRepository):
    model = Withdraw_types
