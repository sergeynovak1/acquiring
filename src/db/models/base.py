import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
import sqlalchemy as sa
from sqlalchemy import Column
from sqlalchemy.orm import Mapped, registry

metadata = sa.MetaData()
mapper_registry = registry(metadata=metadata)
Base = mapper_registry.generate_base()


class BaseEntity(Base):
    __abstract__ = True

    uuid: Mapped[UUID] = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        comment="Идентификатор",
    )

    created_at: Mapped[datetime.datetime] = Column(
        sa.DateTime(timezone=True),
        nullable=False,
        default=sa.func.current_timestamp(),
        comment="Дата создания",
    )

    updated_at: Mapped[datetime.datetime] = Column(
        sa.DateTime(timezone=True),
        nullable=False,
        default=sa.func.current_timestamp(),
        onupdate=sa.func.current_timestamp(),
        comment="Дата обновления",
    )
