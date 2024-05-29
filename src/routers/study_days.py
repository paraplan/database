import uuid
from datetime import date, datetime, timezone

from fastapi import APIRouter
from pydantic import BaseModel

from src.client import db_client
from src.generated_edgedb import AddStudyDayResult, add_study_day

router = APIRouter(tags=["StudyDay"])


class PutStudyDayModel(BaseModel):
    group_full_name: str
    group_name: str
    hour_ids: list[uuid.UUID]
    date: date


@router.put("/study_day", response_model=AddStudyDayResult)
async def put_hour(item: PutStudyDayModel):
    item.date = datetime(item.date.year, item.date.month, item.date.day, tzinfo=timezone.utc)
    return await add_study_day(db_client, **item.model_dump())
