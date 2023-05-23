import uuid

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from typing import Any

Base: Any = declarative_base()


class User(Base):
    """Модель пользователя"""

    __tablename__ = "users"

    user_id:Any = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name:Any = Column(String, nullable=False)
    surname:Any = Column(String, nullable=False)
    email:Any = Column(String, nullable=False, unique=True)
    is_active:Any = Column(Boolean, default=True)
    hashed_password:Any = Column(String, nullable=False)
