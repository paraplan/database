from uuid import UUID

from fastapi import APIRouter

from src.client import db_client
from src.generated_edgedb import (
    InsertSubgroupHourResult,
    SelectSubgroupHoursResult,
    insert_subgroup_hour,
    select_subgroup_hours,
    select_subgroup_hours_by_id,
)

router = APIRouter(prefix="/subgroup_hours", tags=["SubGroupHours"])


@router.get("", response_model=list[SelectSubgroupHoursResult] | SelectSubgroupHoursResult)
async def get_subgroup_hours(id: UUID | None = None):
    if id:
        return await select_subgroup_hours_by_id(db_client, id=id)
    return await select_subgroup_hours(db_client)


@router.put("", response_model=InsertSubgroupHourResult)
async def put_subgroup_hour(cabinet_id: UUID, occupation: str):
    return await insert_subgroup_hour(db_client, cabinet_id=cabinet_id, occupation=occupation)
