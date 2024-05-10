from fastapi import APIRouter
from pydantic import BaseModel

from src.client import db_client
from src.generated_edgedb import InsertGroupResult, SelectGroupsResult, insert_group, select_groups

router = APIRouter(prefix="/groups", tags=["Groups"])


class GroupPutItem(BaseModel):
    name: str
    full_name: str


@router.get("", response_model=list[SelectGroupsResult])
async def get_groups():
    return await select_groups(db_client)


@router.put("", response_model=InsertGroupResult)
async def put_group(item: GroupPutItem):
    return await insert_group(db_client, name=item.name, full_name=item.full_name)
