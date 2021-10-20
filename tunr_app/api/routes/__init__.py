from fastapi import APIRouter
from tunr_app.api.routes.experiments import router as experiments_router


router = APIRouter()


router.include_router(experiments_router, prefix="/experiment", tags=["Experiment"])