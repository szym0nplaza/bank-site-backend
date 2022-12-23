from modules.transactions.application.interfaces import ITransactionRepository
from .queries import GetTransactionsByAccount


def get_transactions(
    dto: GetTransactionsByAccount, repo: ITransactionRepository, **_kwargs
):
    result = repo.get_account_transactions(dto.account_number)
    return result
