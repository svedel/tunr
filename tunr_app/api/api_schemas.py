from enum import Enum
from typing import Optional, Set, Dict, Union, List
from pydantic import BaseModel
from uuid import UUID

# === Basic data models ===
class VarType(str, Enum):
    categorical = "categorical"
    integer = "integer"
    continuous = "continuous"


# class IntVariable(BaseModel):
#     guess: int
#     min: int
#     max: int
#     type: VarType
#
#
# class ContinuousVariable(BaseModel):
#     guess: float
#     min: float
#     max: float
#     type: VarType

class IntOrContVariable(BaseModel):
    guess: Union[int, float]
    min: Union[int, float]
    max: Union[int, float]
    type: VarType


class CategoricalVariable(BaseModel):
    guess: str
    options: Set[str] = set()
    type: VarType


class VariableModel(BaseModel):
    guess: Union[int, float, str]
    min: Optional[Union[int, float]]
    max: Optional[Union[int, float]]
    options: Optional[List[str]]
    type: VarType


# === Data models for endpoints ===
class NewExperiment(BaseModel):
    #covars: Dict[str, Union[IntVariable, ContinuousVariable, CategoricalVariable]]
    #covars: Dict[str, Union[IntOrContVariable, CategoricalVariable]]
    covars: Dict[str, VariableModel]
    model: Optional[str] = None
    acq_func: Optional[str] = None


class AskExperiment(BaseModel):
    exp_id: UUID

