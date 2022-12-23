from modules.transactions.application.ports import AccountsPort
from modules.accounts.infrastructure.facade import AccountsFacade
from modules.transactions.application.dto import TransactionAccountDTO
from typing import Tuple
from decimal import Decimal


class AccountsAdapter(AccountsPort):
    def __init__(self) -> None:
        self.facade = AccountsFacade()

    def get_transaction_accounts(
        self, sender_acc_number: int, receiver_acc_number: int
    ) -> Tuple[TransactionAccountDTO, ...]:
        sender_acc, receiver_acc = self.facade.get_transaction_accounts(
            sender_acc_number, receiver_acc_number
        )
        sender_acc = TransactionAccountDTO(
            currency=sender_acc.default_currency.value,
            number=sender_acc.number,
            balance=sender_acc.balance,
        )
        receiver_acc = TransactionAccountDTO(
            currency=receiver_acc.default_currency.value,
            number=receiver_acc.number,
            balance=receiver_acc.balance,
        )

        return sender_acc, receiver_acc

    def update_accounts_balances(self, sender_account_number: int, receiver_account_number: int, amount: Decimal) -> None:
        self.facade.update_accounts_balances(sender_account_number, receiver_account_number, amount)