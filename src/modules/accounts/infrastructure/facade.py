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
        sender_acc = handle_query(queries.GetAccountByNumber(number=sender_acc_number), self.repo)
        receiver_acc = handle_query(queries.GetAccountByNumber(number=receiver_acc_number), self.repo)
        return sender_acc, receiver_acc

    def update_account_balance(self, acc_number: int, amount: Decimal):
        handle_command(
            commands.UpdateBalance(account_number=acc_number, amount=amount), self.repo
        )

    def get_account_by_number(self, acc_number: int) -> AccountDTO:
        result = handle_query(queries.GetAccountByNumber(number=acc_number), self.repo)
        return result
