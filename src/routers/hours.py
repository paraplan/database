from fastapi import APIRouter
from pydantic import BaseModel, Field

from src.client import db_client
from src.generated_edgedb import (
    AddHourWithCabinetResult,
    add_hour_with_cabinet,
)

router = APIRouter(tags=["Hours"])


class PutHourModel(BaseModel):
    occupation: str
    sub_group: int = Field("1")
    cabinet_number: str
    cabinet_details: str


@router.put("/hour", response_model=AddHourWithCabinetResult)
async def put_hour(item: PutHourModel):
    return await add_hour_with_cabinet(db_client, **item.model_dump())
