"""Таблица миграций alembic."""

from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped

from src.db.models.base import BaseEntity


class AlembicMigrations(BaseEntity):
    __tablename__ = "alembic_migrations"
    __table_args__ = {"extend_existing": True}

    version_name: Mapped[str] = Column(String(200), nullable=False)
    revision: Mapped[str] = Column(String(50), nullable=False)
    down_revision: Mapped[str] = Column(String(50), nullable=False)
    migration_type: Mapped[str] = Column(String(50), nullable=False)
