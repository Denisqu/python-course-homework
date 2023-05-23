from datetime import datetime
from typing import List
from pydantic import BaseModel


class TestSchema(BaseModel):
    id: int | None
    id_task: int | None
    name: str | None
    code: str | None

    class Config:
        orm_mode = True

