from abc import ABC, abstractmethod
from modules.transactions.domain.models import Transaction
from base.types import Repository


class ITransactionRepository(ABC, Repository):
    @abstractmethod
    def create_transaction(self, transaction: Transaction) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_account_transactions(self, account_number: int) -> None:
        """Searches transaction for given account by `sender_account`"""
        raise NotImplementedError