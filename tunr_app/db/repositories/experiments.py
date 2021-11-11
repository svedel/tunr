from tunr_app.db.repositories.base import BaseRepository
from tunr_app.schemas.experiments import NewExperimentInDB, NewExperimentCreate


CREATE_EXPERIMENT_QUERY = """
INSERT INTO experiments (model, acq_func, exp_name, exp_description)
VALUES (:model, :acq_func, :exp_name, :exp_description)
RETURNING exp_id, exp_name, description, timestamp, exp_entry_id, exp_iteration_count, model, acq_func; 
"""

class NewExperimentsRepository(BaseRepository):
    """
    All database actions associated with the NewExperiment resource
    """
    async def create_new_experiment(self, *, new_experiment: NewExperimentCreate) -> NewExperimentInDB:
        query_values = new_experiment.dict()
        experiment = await self.db.fetch_one(query=CREATE_EXPERIMENT_QUERY, values=query_values)

        return NewExperimentInDB(**experiment)
