from fastapi import FastAPI

from src.api.users.handlers import user_router

app = FastAPI(
    title='Crm',
    version='1',
)
