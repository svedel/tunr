from fastapi import FastAPI
from tunr_app.api.routes import router as api_router


tags_metadata = [
    {
        "name": "Experiment",
        "description": "Operations for experiments.",
    }
]


def get_application():
    app = FastAPI(title="Tunr", version="1.0.0", openapi_tags=tags_metadata)

    app.include_router(api_router)

    return app


app = get_application()


# === get next experiment ===
