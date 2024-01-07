import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from src.models.base import Base
from ..config.settings import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True)

# This will be used to create new sessions
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def init_db() -> None:
    """
    Initializes the database by creating all tables defined in the metadata.

    Returns:
        None
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
