# app/models/user.py
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy_serializer import SerializerMixin

from app.models.entities.base import Base


class User(Base, SerializerMixin):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50), nullable=False)
  email = Column(String(100), unique=True)
  created_at = Column(DateTime, server_default=func.now())