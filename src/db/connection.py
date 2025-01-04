from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine


class AsyncDatabase:
    def __init__(self, db_uri: str) -> None:
        self._db_uri = db_uri
        self._engine: AsyncEngine | None = None

    async def connect(self, **kwargs):
        self._engine = create_async_engine(self._db_uri, **kwargs)

    async def disconnect(self):
        await self._engine.dispose()

    @property
    def engine(self):
        return self._engine
