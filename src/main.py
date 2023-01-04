import uvicorn
from fastapi import FastAPI

from config.settings import settings
from modules.accounts.entrypoints.routers import accounts_router
from modules.transactions.entrypoints.routers import transactions_router

app = FastAPI()
app.include_router(accounts_router, prefix="/api", tags=["Users/Accounts API"])
app.include_router(transactions_router, prefix="/api", tags=["Transactions API"])


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.application_host,
        log_level="debug",
        reload=True,
        port=8000,
    )