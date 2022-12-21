from modules.transactions.application.interfaces import ITransactionRepository
from modules.transactions.application.ports import AccountsPort
from modules.transactions.domain.models import Transaction
from typing import List, Tuple
from modules.transactions.application.dto import TransactionAccountDTO
from decimal import Decimal


def account_fixture():
    return (
        TransactionAccountDTO(
            currency="EUR",
            number=123456789012,
            balance=Decimal("1000.00"),
        ),
        TransactionAccountDTO(
            currency="EUR",
            number=998765432109,
            balance=Decimal("500.00"),
        ),
    )


class TransactionsMockRepo(ITransactionRepository):
    transactions: List[Transaction] = []

    def create_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)


class AccountsMockAdapter(AccountsPort):
    def get_transaction_accounts(
        self, _sender_acc_number: int, _receiver_acc_number: int
    ) -> Tuple[TransactionAccountDTO, ...]:
        return account_fixture()
