from pydantic import BaseModel
from uuid import UUID


class CoreModel(BaseModel):
    """
    Any common logic to be shared across all models goes here
    """
    pass