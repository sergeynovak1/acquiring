import uuid
from typing import Protocol, TypeVar, final

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.base import Base

ModelT = TypeVar("ModelT", bound=Base)


class BaseAsyncRepository:
    model: ModelT

    @final
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    @final
    def add(self, item: ModelT):
        self.session.add(item)

    @final
    async def add_many(self, items: list[ModelT]):
        self.session.add_all(items)

    @final
    async def delete(self, item: ModelT):
        await self.session.delete(item)

    @final
    async def get_by_id(self, id_: uuid.UUID) -> ModelT | None:
        stmt = select(self.model).where(self.model.id == id_)
        result = await self.session.execute(stmt)
        return result.scalar()
