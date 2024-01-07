from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Text, JSON
from sqlalchemy.orm import declarative_base, relationship, deferred
from .base import Base


class Video(Base):
    """The Video class corresponds to the "Videos" database table."""

    __tablename__ = "Videos"

    video_id = Column(String, primary_key=True)
    platform = Column(String, nullable=False)
    url = Column(String, nullable=False)
    create_date = Column(Integer, nullable=False)
    transcript = deferred(Column(JSON, nullable=False))

    # Relationship to BestOfs
    bestofs = relationship("BestOf", back_populates="video")
