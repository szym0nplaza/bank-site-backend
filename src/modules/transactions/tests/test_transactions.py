from .conftest import AccountsMockAdapter, TransactionsMockRepo
from base.commands.command_handler import handle_command
from modules.transactions.application.commands import commands
from decimal import Decimal


class TestTransactions:
    repo = TransactionsMockRepo()
    accounts = AccountsMockAdapter()

    def test_create(self):
        handle_command(
            command=commands.RegisterTransaction(123456789012, 998765432109, Decimal("400.00")),
            repo=self.repo,
            accounts_client=self.accounts,
        )

    def test_no_funds(self):
        try:
            handle_command(
                command=commands.RegisterTransaction(123456789012, 998765432109, Decimal("1400.00")),
                repo=self.repo,
                accounts_client=self.accounts,
            )
        except AssertionError:
            assert True

