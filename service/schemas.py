from typing_extensions import Annotated
from pydantic import BaseModel, Field


class Asset(BaseModel):
    id: int
    value: Annotated[int, Field(strict=True, ge=1, le=5)]
