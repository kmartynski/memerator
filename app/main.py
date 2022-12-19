from fastapi import FastAPI

from .routers import health, memes


def create_app():
    app = FastAPI()

    app.include_router(health.router)
    app.include_router(memes.router)
    return app


create_app()
