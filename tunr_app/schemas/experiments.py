from enum import Enum
from typing import Optional, Set, Dict, Union, List
#from sqlalchemy.dialects.postgresql import JSON
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

from tunr_app.schemas.core import CoreModel


# === Basic data services ===
class ExperimentCoreModel(CoreModel):
    """
    Any common logic to be shared among Experiment goes here
    """
    pass


class IDExperimentMixin(BaseModel):
    exp_id: UUID


class CovarType(str, Enum):
    categorical = "categorical"
    integer = "integer"
    continuous = "continuous"


# class IntVariable(ExperimentCoreModel):
#     guess: int
#     min: int
#     max: int
#     type: CovarType
#
#
# class ContinuousVariable(ExperimentCoreModel):
#     guess: float
#     min: float
#     max: float
#     type: CovarType

class IntOrContVariable(ExperimentCoreModel):
    guess: Union[int, float]
    min: Union[int, float]
    max: Union[int, float]
    type: CovarType


class CategoricalVariable(ExperimentCoreModel):
    guess: str
    options: Set[str] = set()
    type: CovarType


class VariableModel(ExperimentCoreModel):
    guess: Union[int, float, str]
    min: Optional[Union[int, float]]
    max: Optional[Union[int, float]]
    options: Optional[List[str]]
    type: CovarType = "continuous"


# === New Experiment ===
class NewExperiment(ExperimentCoreModel):
    #covars: Dict[str, Union[IntVariable, ContinuousVariable, CategoricalVariable]]
    #covars: Dict[str, Union[IntOrContVariable, CategoricalVariable]]
    #covars: Dict[str, VariableModel]
    model: Optional[str] = None
    acq_func: Optional[str] = None
    exp_name: str = "My model tuning experiment"
    exp_description: Optional[str] = "This is the best experiment"


class NewExperimentCreate(NewExperiment):
    exp_iteration_count: int = 0


class NewExperimentInDB(IDExperimentMixin, NewExperiment):
    #covars: JSON
    timestamp: datetime
    exp_entry_id: int
    exp_iteration_count: int


class NewExperimentPublic(IDExperimentMixin, NewExperiment):
    timestamp: datetime
    exp_entry_id: int
    exp_iteration_count: int


class AskExperiment(IDExperimentMixin):
    pass