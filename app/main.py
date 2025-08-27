import logging
import sys

from fastapi import FastAPI

from app.api import users

log_format = "%(asctime)s | %(levelname)-8s | %(name)-12s - %(message)s"
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=log_format)

app = FastAPI(title="Python FastAPI Template", version="0.1.0")

app.include_router(users.router, prefix="/api/v1/users", tags=["User"])
