from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.core.config import Config

engine = create_async_engine(Config.get_database_url())

SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

class Base(DeclarativeBase):
    pass

async def get_db():
    """
    Provide a transactional asynchronous database session generator.
    
    Yields:
        AsyncSession: an active async SQLAlchemy session from the session factory.
    
    Description:
        Commits the transaction after the caller finishes using the session. If an exception occurs while the caller uses the session, rolls back the transaction and re-raises the exception. The session is always closed when finished.
    """
    async with SessionLocal() as db:
        try:
            yield db
            await db.commit()
        except: 
            await db.rollback()
            raise
        finally:
            await db.close()