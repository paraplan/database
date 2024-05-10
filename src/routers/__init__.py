from typing import Iterable

from fastapi import APIRouter

from . import cabinet, groups, hours, study_days, subgroup_hours

routers: Iterable[APIRouter] = (
    cabinet.router,
    subgroup_hours.router,
    hours.router,
    groups.router,
    study_days.router,
)
