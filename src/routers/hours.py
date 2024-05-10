from uuid import UUID

from fastapi import APIRouter
from pydantic import BaseModel

from src.client import db_client
from src.generated_edgedb import (
    InsertHourResult,
    SelectHourByIdResult,
    insert_hour,
    select_hour_by_id,
    select_hours,
)

router = APIRouter(prefix="/hours", tags=["Hours"])


class HourPutItem(BaseModel):
    sub_group_id: list[UUID]


@router.get("", response_model=list[SelectHourByIdResult] | SelectHourByIdResult)
async def get_hours(id: UUID | None = None):
    if id:
        return await select_hour_by_id(db_client, id=id)
    return await select_hours(db_client)


@router.put("", response_model=InsertHourResult)
async def put_hour(item: HourPutItem):
    return await insert_hour(db_client, sub_group_id=item.sub_group_id)
