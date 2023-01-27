from base.commands.command_handler import handle_command
from base.queries.query_handler import handle_query
from modules.loans.application.commands import commands
from modules.loans.application.queries import queries
from .conftest import LoanMockRepository
from decimal import Decimal


class TestLoans:
    repo = LoanMockRepository()

    def test_loan_register(self):
        result = handle_command(
            commands.RegisterLoan(
                user_id=1,
                account_number=123456789012,
                borrowed_amount=Decimal("20000.00"),
                no_installments=10,
            ),
            self.repo,
        )

        assert result.status == 201
        assert result.message == "ok"

    def test_loans_get(self):
        result = handle_query(queries.GetLoans(1), self.repo)
        assert result[0].account_number == 123456789012
        assert result[0].borrowed_amount == Decimal("20000.00")
        assert result[0].no_installments == 10
        assert str(result[0].status) == "active"
