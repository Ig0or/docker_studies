from sqlalchemy import Column, String, Integer

from src.infrastructure.mysql.base import Base


class UsersModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self) -> str:
        return f"Users [name={self.name}]"
