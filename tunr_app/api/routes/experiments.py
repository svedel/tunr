from uuid import UUID
from fastapi import APIRouter, Body, Depends
from starlette.status import HTTP_201_CREATED

from tunr_app.services.user_services import create_exp_id
from tunr_app.schemas.experiments import NewExperiment, NewExperimentPublic, NewExperimentCreate
from tunr_app.services.data_validation import validate_exp_id
from tunr_app.api.dependencies.database import get_repository
from tunr_app.db.repositories.experiments import NewExperimentsRepository


router = APIRouter()


# === Create new experiment ===
@router.post("/new", tags=["Experiment"])
async def create_new_experiment(new_exp: NewExperiment):
    """
    create new experiment
    """

    # create experiment id
    exp_id = create_exp_id()

    op = {**new_exp.dict(), "exp_id": exp_id, }
    return op


@router.post("/new_full", response_model=NewExperimentPublic, name="experiments:create_new_experiment", status_code=HTTP_201_CREATED)
async def create_new_experiment_full(
        new_experiment: NewExperimentCreate = Body(..., embed=True),
        experiments_repo: NewExperimentsRepository = Depends(get_repository(NewExperimentsRepository)),
) -> NewExperimentPublic:
    created_experiment = await experiments_repo.create_new_experiment(new_experiment=new_experiment)

    return created_experiment


# === get next experiment ===
@router.get("/ask/{exp_id}", tags=["Experiment"])
def ask_new_exp(exp_id: UUID):
    """
    get next experiment proposal
    """

    # validate experiment_id
    valid_exp_id = validate_exp_id(exp_id)

    # load saved exp

    # retrieve next exp proposal

    return {"exp_id": exp_id, "exp_iter": 1}