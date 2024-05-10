from datetime import datetime
from uuid import UUID

from fastapi import APIRouter

from src.client import db_client
from src.generated_edgedb import (
    InsertStudyDayResult,
    SelectStudyDaysResult,
    insert_study_day,
    select_study_days,
)

router = APIRouter(prefix="/study_days", tags=["StudyDays"])


@router.get("", response_model=list[SelectStudyDaysResult])
async def get_study_days():
    return await select_study_days(db_client)


@router.put("", response_model=InsertStudyDayResult)
async def put_study_day(date: datetime, group_id: UUID, hour_ids: list[UUID]):
    return await insert_study_day(db_client, date=date, group_id=group_id, hour_ids=hour_ids)
