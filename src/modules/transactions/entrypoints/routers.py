from fastapi import APIRouter
from fastapi.responses import JSONResponse
from modules.transactions.application.commands.commands import RegisterTransaction
from modules.transactions.application.queries.queries import GetTransactionsByAccount
from modules.transactions.infrastructure.repositories import TransactionRepository
from modules.transactions.infrastructure.adapters import AccountsAdapter
from base.commands.command_handler import handle_command
from base.queries.query_handler import handle_query


transactions_router = router = APIRouter()


@router.post("/create-transaction")
async def register_transaction(dto: RegisterTransaction):
    response = handle_command(
        dto, TransactionRepository(), accounts_client=AccountsAdapter()
    )
    return JSONResponse(response.message, status_code=response.status)


@router.get("/transactions/{acc_number}")
async def get_transactions(acc_number: int):
    response = handle_query(
        GetTransactionsByAccount(account_number=acc_number), TransactionRepository()
    )
    return response
