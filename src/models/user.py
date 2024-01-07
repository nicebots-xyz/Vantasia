from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship
from .base import Base


class User(Base):
    """The User class corresponds to the "Users" database table."""

    __tablename__ = "Users"

    user_id = Column(Integer, primary_key=True)
    join_date = Column(Integer, nullable=False)
    last_used_date = Column(Integer, nullable=False)
    tos_hash_accepted = Column(String, nullable=True)

    # Relationship to bestofs
    bestofs = relationship("BestOf", back_populates="creator")
    channels = relationship("Channel", back_populates="claimer")
