from fastapi import FastAPI

from api.controllers.controller import api_router
from . import settings, VERSION


def create_api() -> FastAPI:
    """This method generates the API server"""

    app = FastAPI(
        title=settings.api_name,
        version=VERSION,
    )

    app.include_router(api_router)

    return app