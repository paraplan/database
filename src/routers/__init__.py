from typing import Iterable

from fastapi import APIRouter

from . import cabinet, hours, subgroup_hours

routers: Iterable[APIRouter] = (
    cabinet.router,
    subgroup_hours.router,
    hours.router,
)
