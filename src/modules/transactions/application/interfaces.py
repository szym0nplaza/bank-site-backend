from abc import ABC, abstractmethod
from modules.transactions.domain.models import Transaction
from base.types import Repository


class ITransactionRepository(ABC, Repository):
    @abstractmethod
    def create_transaction(self, transaction: Transaction) -> None:
        raise NotImplementedError