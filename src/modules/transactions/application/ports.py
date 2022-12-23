from abc import ABC, abstractmethod
from typing import Tuple
from modules.transactions.application.dto import TransactionAccountDTO
from decimal import Decimal


class AccountsPort(ABC):
    @abstractmethod
    def get_transaction_accounts(
        self, sender_acc_number: int, receiver_acc_number: int
    ) -> Tuple[TransactionAccountDTO, ...]:
        raise NotImplementedError

    @abstractmethod
    def update_accounts_balances(
        self, sender_account_number: int, receiver_account_number: int, amount: Decimal
    ) -> None:
        raise NotImplementedError
