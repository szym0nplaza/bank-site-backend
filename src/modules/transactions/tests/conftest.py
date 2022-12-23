from modules.transactions.application.interfaces import ITransactionRepository
from modules.transactions.application.ports import AccountsPort
from modules.transactions.domain.models import Transaction
from typing import List, Tuple
from modules.transactions.application.dto import TransactionAccountDTO
from decimal import Decimal


class Accounts:
    sender_acc = TransactionAccountDTO(
        currency="EUR",
        number=123456789012,
        balance=Decimal("1000.00"),
    )
    receiver_acc = TransactionAccountDTO(
        currency="EUR",
        number=998765432109,
        balance=Decimal("500.00"),
    )

    @classmethod
    def accounts(cls) -> Tuple[TransactionAccountDTO, ...]:
        return cls.sender_acc, cls.receiver_acc


class TransactionsMockRepo(ITransactionRepository):
    transactions: List[Transaction] = []

    def create_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)

    def get_account_transactions(self, account_number: int) -> list:
        transactions = list(
            filter(lambda x: x.sender_account == account_number, self.transactions)
        )
        return transactions


class AccountsMockAdapter(AccountsPort):
    def get_transaction_accounts(
        self, _sender_acc_number: int, _receiver_acc_number: int
    ) -> Tuple[TransactionAccountDTO, ...]:
        return Accounts.accounts()

    def update_accounts_balances(
        self, _sender_account_number: int, _receiver_account_number: int, amount: Decimal
    ) -> None:
        Accounts.sender_acc.balance -= amount
        Accounts.receiver_acc.balance += amount
