from abc import ABC, abstractmethod


class AccountsPort(ABC):
    @abstractmethod
    def get_transaction_accounts(
        self, sender_acc_number: int, receiver_acc_number: int
    ):
        raise NotImplementedError