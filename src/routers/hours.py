from fastapi import APIRouter
from pydantic import BaseModel, Field

from src.client import db_client
from src.generated_edgedb import (
    AddHourResult,
    add_hour,
    add_hour_with_cabinet,
)

router = APIRouter(tags=["Hours"])


class PutHourModel(BaseModel):
    occupation: str
    number: int
    sub_group: int = Field("1")
    cabinet_number: str | None = None
    cabinet_details: str | None = None


@router.put("/hour", response_model=AddHourResult)
async def put_hour(item: PutHourModel):
    if item.cabinet_number is not None and item.cabinet_details is not None:
        return await add_hour_with_cabinet(db_client, **item.model_dump())
    return await add_hour(
        db_client,
        occupation=item.occupation,
        number=item.number,
        sub_group=item.sub_group,
    )
