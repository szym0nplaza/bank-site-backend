from fastapi import FastAPI
from modules.accounts.entrypoints.routers import accounts_router


app = FastAPI()
app.include_router(accounts_router)
