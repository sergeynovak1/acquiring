import asyncio
import logging

from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models import AlembicMigrations


class DBLoggingHandler(logging.Handler):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def emit(self, record):
        loop = asyncio.get_event_loop()
        if loop.is_running():
            loop.create_task(self._handle_emit(record))
        else:
            loop.run_until_complete(self._handle_emit(record))

    async def _handle_emit(self, record):
        message = self.format(record)
        revision, down_revision, version_name, migration_type = (
            self.parse_migration_message(message)
        )
        if revision and down_revision and version_name and migration_type:
            try:
                migration = AlembicMigrations(
                    version_name=version_name,
                    revision=revision,
                    down_revision=down_revision,
                    migration_type=migration_type,
                )

                self.session.add(migration)
            except Exception as e:
                print(f"Ошибка при сохранении миграции: {e}")

    def parse_migration_message(self, message):
        # Парсинг для строки вида: INFO - Running downgrade c3dfc3fedb2f -> 6d8f06c9a685, add models
        try:
            if "Running downgrade" in message or "Running upgrade" in message:
                parts = message.split(", ")
                migration_info = parts[0].split(" ")
                migration_type = migration_info[3]
                revision = migration_info[4] if len(migration_info) > 4 else None
                down_revision = migration_info[6] if len(migration_info) > 4 else None
                version_name = parts[1] if len(parts) > 1 else None

                return revision, down_revision, version_name, migration_type
        except Exception as e:
            print(f"Ошибка парсинга сообщения: {e}")
        return None, None, None, None


def setup_alembic_logging(session: AsyncSession):
    alembic_logger = logging.getLogger("alembic")
    handler = DBLoggingHandler(session)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    alembic_logger.handlers = []
    alembic_logger.addHandler(handler)
