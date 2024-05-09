from typing import Iterable

from fastapi import APIRouter

from . import cabinet, subgroup_hours

routers: Iterable[APIRouter] = (
    cabinet.router,
    subgroup_hours.router,
)
