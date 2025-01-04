from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton

from src.core.config.settings import db_settings
from src.db.connection import AsyncDatabase


class BaseContainer(DeclarativeContainer):
    db = Singleton(AsyncDatabase, db_uri=db_settings.uri)
