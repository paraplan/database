from uuid import UUID

from fastapi import APIRouter
from pydantic import BaseModel

from src.client import db_client
from src.generated_edgedb import (
    DeleteCabinetResult,
    GetCabinetResult,
    delete_cabinet,
    get_cabinet,
    insert_or_select_cabinet,
)

router = APIRouter(prefix="/cabinets", tags=["Cabinet"])


@router.get("", response_model=list[GetCabinetResult])
async def get_cabinets():
    return await get_cabinet(db_client)


class PutCabinetModel(BaseModel):
    name: str
    room: str


@router.put("", response_model=DeleteCabinetResult)
async def put_cabinet(item: PutCabinetModel | list[PutCabinetModel]):
    if not isinstance(item, list):
        return await insert_or_select_cabinet(db_client, name=item.name, room=item.room)
    response = []
    for cabinet in item:
        response.append(
            await insert_or_select_cabinet(db_client, name=cabinet.name, room=cabinet.room)
        )
    return response


@router.delete("", response_model=DeleteCabinetResult)
async def remove_cabinet(cabinet_id: UUID):
    return await delete_cabinet(db_client, cabinet_id=cabinet_id)
