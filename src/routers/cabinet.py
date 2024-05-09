from uuid import UUID

from fastapi import APIRouter

from src.client import db_client
from src.generated_edgedb import (
    DeleteCabinetResult,
    GetCabinetResult,
    delete_cabinet,
    get_cabinet,
    insert_cabinet,
)

router = APIRouter(prefix="/cabinet", tags=["Cabinet"])


@router.get("", response_model=list[GetCabinetResult])
async def get_cabinets():
    return await get_cabinet(db_client)


@router.put("", response_model=DeleteCabinetResult)
async def put_cabinet(name: str, room: str):
    return await insert_cabinet(db_client, name=name, room=room)


@router.delete("", response_model=DeleteCabinetResult)
async def remove_cabinet(cabinet_id: UUID):
    return await delete_cabinet(db_client, cabinet_id=cabinet_id)
