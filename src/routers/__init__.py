from typing import Iterable

from fastapi import APIRouter

from . import hours, study_days

routers: Iterable[APIRouter] = (hours.router, study_days.router)
