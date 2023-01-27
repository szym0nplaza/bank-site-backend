from .commands import RegisterLoan
from modules.loans.application.interfaces import ILoanRepository
from modules.loans.domain.models import Loan


def add_loan(dto: RegisterLoan, repo: ILoanRepository) -> None:
    loan = Loan(**dto.__dict__)
    with repo:
        repo.register_loan(loan)