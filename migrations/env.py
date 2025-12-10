from app.core.config import Config
import asyncio
from logging.config import fileConfig

from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy import pool
from alembic import context

import os
from app.core.database import Base

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

config.set_main_option("sqlalchemy.url", Config.get_database_url())

target_metadata = Base.metadata

def run_migrations_offline():
    context.configure(url=Config.get_database_url(), literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    from sqlalchemy.ext.asyncio import create_async_engine
    engine = create_async_engine(Config.get_database_url(), poolclass=pool.NullPool)

    async with engine.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await engine.dispose()

if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
