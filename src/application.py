from fastapi import FastAPI

from src.core.config import settings
from src.core.fastapi.routes import add_routes
from src.dependency.container import Container


def create_app() -> FastAPI:
    container = Container()

    app = FastAPI(
        title="ACQUIRING SERVICE API",
        version=settings.application_settings.app_version,
        openapi_url="/api/acquiring-emulator/openapi.json",
        description="Acquiring service",
        docs_url="/api/acquiring-emulator/docs",
    )
    app.container = container

    add_routes(app)

    return app


app = create_app()
