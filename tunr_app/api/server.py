from fastapi import FastAPI
from uuid import UUID
from tunr_app.services.user_services import create_exp_id
from tunr_app.api.api_schemas import NewExperiment
from tunr_app.services.data_validation import validate_exp_id


app = FastAPI(title="Tunr", version="1.0.0")


# === Create new experiment ===
@app.post("/new_experiment")
async def create_new_experiment(new_exp: NewExperiment):
    """
    create new experiment
    """

    # create experiment id
    exp_id = create_exp_id()

    op = {**new_exp.dict(), "exp_id": exp_id, }
    return op


# === get next experiment ===
@app.get("/ask/{exp_id}")
def ask_new_exp(exp_id: UUID):
    """
    get next experiment proposal
    """

    # validate experiment_id
    valid_exp_id = validate_exp_id(exp_id)

    # load saved exp

    # retrieve next exp proposal

    return {"exp_id": exp_id, "exp_iter": 1}


# === get next experiment ===
