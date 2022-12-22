from modules.transactions.application.interfaces import ITransactionRepository
from modules.transactions.domain.models import Transaction
from config.settings import ESClient


class TransactionRepository(ITransactionRepository):
    TRANSACTION_INDEX = "transactions"

    def __init__(self, es_client: ESClient = ESClient()):
        self.es_client = es_client

    def create_transaction(self, transaction: Transaction) -> None:
        self.es_client.index(transaction.__dict__, self.TRANSACTION_INDEX)

    def get_account_transactions(self, account_number: int) -> list:
        return self.es_client.search(
            {"sender_account": account_number}, self.TRANSACTION_INDEX
        )
