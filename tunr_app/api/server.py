from fastapi import FastAPI
from tunr_app.api.routes import router as api_router
from tunr_app.core import config, tasks

tags_metadata = [
    {
        "name": "Experiment",
        "description": "Operations for experiments.",
    }
]


def get_application():
    app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION, openapi_tags=tags_metadata)

    # create and shut down database connection on app start and stop
    app.add_event_handler("startup", tasks.create_start_app_handler(app))
    app.add_event_handler("shutdown", tasks.create_stop_app_handler(app))

    app.include_router(api_router)

    return app


app = get_application()


# === get next experiment ===
