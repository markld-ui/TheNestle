import os
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

from models.user_model import Model

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    poolclass=NullPool
)
new_session = async_sessionmaker(engine, expire_on_commit=False)

async def create_tables():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Model.metadata.create_all)
        print("Таблицы успешно созданы")
    except Exception as e:
        print(f"Ошибка при создании таблиц: {e}")

async def delete_tables():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Model.metadata.drop_all)
        print("Таблицы успешно удалены")
    except Exception as e:
        print(f"Ошибка при удалении таблиц: {e}")