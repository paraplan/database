from uuid import UUID

from edgedb import ConstraintViolationError
from fastapi import APIRouter
from pydantic import BaseModel

from src.client import db_client
from src.generated_edgedb import (
    DeleteCabinetResult,
    SelectCabinetByRoomResult,
    SelectCabinetsResult,
    delete_cabinet,
    insert_cabinet,
    select_cabinet_by_room,
    select_cabinets,
)

router = APIRouter(prefix="/cabinet", tags=["Cabinet"])


class CabinetPutItem(BaseModel):
    name: str
    room: str


@router.get("", response_model=list[SelectCabinetsResult])
async def get_cabinets():
    return await select_cabinets(db_client)


@router.put("", response_model=DeleteCabinetResult | SelectCabinetByRoomResult)
async def put_cabinet(item: CabinetPutItem):
    try:
        return await insert_cabinet(db_client, name=item.name, room=item.room)
    except ConstraintViolationError:
        return await select_cabinet_by_room(db_client, room=item.room)


@router.delete("", response_model=DeleteCabinetResult)
async def remove_cabinet(cabinet_id: UUID):
    return await delete_cabinet(db_client, cabinet_id=cabinet_id)
