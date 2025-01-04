from pydantic import Field

from src.core.config.base import BaseSettings


class ApplicationSettings(BaseSettings):
    api_prefix: str = "/api/acquiring-emulator/v1"
    app_version: str = "1.1.0"

    class Config:
        extra = "ignore"


class LogSettings(BaseSettings):
    level: str = Field(default="WARNING", alias="LOG_LEVEL")


class DatabaseSettings(BaseSettings):
    dialect: str = "postgresql"

    db_user: str = "postgres"
    db_pass: str = "1"
    db_host: str = "127.0.0.1"
    db_port: str = "5432"
    db_name: str = "acquiring"

    @property
    def uri(self):
        db_name = self.db_name
        return f"{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{db_name}"

    @property
    def dsn_no_driver(self) -> str:
        """Возвращает dsn при отсутсвии драйвера бд.

        Returns:
            dsn_no_driver
        """
        return f"{self.dialect}://{self.uri}"

    @property
    def dsn(self) -> str:
        """Возвращает dsn.

        Returns:
            dsn
        """
        return f"{self.dialect}+psycopg://{self._uri}"

    @property
    def alembic_dsn(self) -> str:
        return f"{self.dialect}+asyncpg://{self._uri}"

    class Config:
        extra = "ignore"


db_settings = DatabaseSettings()
application_settings = ApplicationSettings()
log_settings = LogSettings()
