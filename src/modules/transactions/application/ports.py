from abc import ABC, abstractmethod
from typing import Tuple
from modules.transactions.application.dto import TransactionAccountDTO


class AccountsPort(ABC):
    @abstractmethod
    def get_transaction_accounts(
        self, sender_acc_number: int, receiver_acc_number: int
    ) -> Tuple[TransactionAccountDTO, ...]:
        raise NotImplementedError