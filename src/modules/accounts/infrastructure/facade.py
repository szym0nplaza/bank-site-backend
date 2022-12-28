from typing import Tuple

from base.queries.query_handler import handle_query
from base.commands.command_handler import handle_command
from base.types import Facade
from modules.accounts.application.dto import AccountDTO
from modules.accounts.application.queries import queries
from modules.accounts.application.commands import commands
from decimal import Decimal

from .repositories import ClientRepository


class AccountsFacade(Facade):
    def __init__(self) -> None:
        self.repo = ClientRepository()

    def get_transaction_accounts(
        self, sender_acc_number: int, receiver_acc_number: int
    ) -> Tuple[AccountDTO, AccountDTO]:
        """Returns `(sender_account, receiver_account)` tuple for further operations"""
        dto = queries.GetTransactionAccounts(
            sender_acc_number=sender_acc_number, receiver_acc_number=receiver_acc_number
        )
        result = handle_query(dto, self.repo)
        return result

    def update_account_balance(self, acc_number: int, amount: Decimal):
        handle_command(commands.UpdateBalance(account_number=acc_number, amount=amount), self.repo)
