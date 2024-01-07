from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship
from .base import Base


class Channel(Base):
    """The Channel class corresponds to the "Channels" database table."""

    __tablename__ = "Channels"

    channel_id = Column(String, primary_key=True)
    platform = Column(String, nullable=False)
    identification_str = Column(String, nullable=False)
    claimer_id = Column(Integer, ForeignKey("Users.user_id"), nullable=True)

    claimer = relationship("User", back_populates="channels")
