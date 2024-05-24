from typing import Iterable

from fastapi import APIRouter

from . import hours

routers: Iterable[APIRouter] = (hours.router,)
