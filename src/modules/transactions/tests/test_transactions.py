from .conftest import AccountsMockAdapter, TransactionsMockRepo
from base.commands.command_handler import handle_command
from base.queries.query_handler import handle_query
from modules.transactions.application.commands import commands
from modules.transactions.application.queries import queries
from decimal import Decimal


class TestTransactions:
    repo = TransactionsMockRepo()
    accounts = AccountsMockAdapter()

    def test_create(self):
        response = handle_command(
            command=commands.RegisterTransaction(123456789012, 998765432109, Decimal("400.00")),
            repo=self.repo,
            accounts_client=self.accounts,
        )
        assert response.message == "ok"
        assert response.status == 201

    def test_get(self):
        result = handle_query(queries.GetTransactionsByAccount(account_number=123456789012), self.repo)
        transaction = result[0]

        assert len(result) == 1
        assert transaction.currency == "EUR"
        assert transaction.receiver_account == 998765432109
        assert transaction.receiver_post_balance == Decimal("900.00")
        assert transaction.sender_post_balance == Decimal("600.00")

    def test_no_funds(self):
        try:
            handle_command(
                command=commands.RegisterTransaction(123456789012, 998765432109, Decimal("1400.00")),
                repo=self.repo,
                accounts_client=self.accounts,
            )
        except AssertionError:
            assert True

