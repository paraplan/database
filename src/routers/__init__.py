from typing import Iterable

from fastapi import APIRouter

from . import cabinet

routers: Iterable[APIRouter] = (cabinet.router,)
