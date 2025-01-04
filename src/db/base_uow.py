from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession


class AsyncBaseUnitOfWork:
    def __init__(self, engine: AsyncEngine) -> None:
        self.engine = engine
        self.session: AsyncSession | None = None
        self.reuse_session: bool = False

    def __call__(self, *, reuse_session: bool = False):
        self.reuse_session = reuse_session
        return self

    async def __aenter__(self):
        if not self.session or not self.reuse_session:
            self.session = AsyncSession(self.engine)

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        traceback,
    ):
        if not self.reuse_session:
            if exc_type:
                await self.rollback()

            await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def flush(self):
        await self.session.flush()

    async def refresh(self, item):
        await self.session.refresh(item)

    async def rollback(self):
        await self.session.rollback()
