import sqlalchemy

from sqlalchemy import (
    create_engine,
    Column,
    String,
    Integer,
    ForeignKey,
    Text,
    JSON,
)
from sqlalchemy.orm import declarative_base, relationship, deferred
from .base import Base


class BestOf(Base):
    """The BestOf class corresponds to the "BestOfs" database table."""

    __tablename__ = "BestOfs"
    bestof_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    video_id = Column(String, ForeignKey("Videos.video_id"))
    create_date = Column(Integer, nullable=False)
    BESTOF_INDEXES = deferred(Column(JSON))
    JSON_OTL = deferred(Column(JSON))  # NOTE: Deprecated, the JSON_OTL column is no longer used since it is recreated every time a bestof is called with the framerate given by the user.
    creator_id = Column(Integer, ForeignKey("Users.user_id"), nullable=True)

    # Relationships
    video = relationship("Video", back_populates="bestofs")
    creator = relationship("User", back_populates="bestofs")
