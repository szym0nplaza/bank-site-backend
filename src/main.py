from fastapi import FastAPI
import uvicorn
from modules.accounts.entrypoints.routers import accounts_router
from modules.transactions.entrypoints.routers import transactions_router


app = FastAPI()
app.include_router(accounts_router, prefix="/api", tags=["Users/Accounts API"])
app.include_router(transactions_router, prefix="/api", tags=["Transactions API"])
