from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, mapped_column


class BaseModel(DeclarativeBase):
    id = mapped_column(Integer, autoincrement=True, unique=True, primary_key=True)
