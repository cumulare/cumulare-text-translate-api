from importlib import metadata
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from fastapi.staticfiles import StaticFiles




from cumulare_text_translate_api.logging import configure_logging
from cumulare_text_translate_api.web.api.router import api_router
from cumulare_text_translate_api.web.gql.router import gql_router
from cumulare_text_translate_api.web.lifetime import (
    register_shutdown_event,
    register_startup_event,
)

APP_ROOT = Path(__file__).parent.parent


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    configure_logging()
    app = FastAPI(
        title="cumulare_text_translate_api",
        version=metadata.version("cumulare_text_translate_api"),
        docs_url=None,
        redoc_url=None,
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    # add longer timeout for slow requests
    app.timeout_keep_alive = 60

    # Adds startup and shutdown events.
    register_startup_event(app)
    from fastapi.middleware.cors import CORSMiddleware

    register_shutdown_event(app)

    
    # allow json responses
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["GET", "POST"],
        allow_headers=["*"],
    )

    # Main router for the API.
    app.include_router(router=api_router, prefix="/api")
    # Graphql router
    app.include_router(router=gql_router, prefix="/graphql")
    # Adds static directory.
    # This directory is used to access swagger files.
    app.mount(
        "/static",
        StaticFiles(directory=APP_ROOT / "static"),
        name="static",
    )

    return app
