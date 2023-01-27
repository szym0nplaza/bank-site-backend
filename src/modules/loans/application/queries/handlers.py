from .queries import GetLoans
from modules.loans.application.interfaces import ILoanRepository
from modules.loans.application.dto import LoanDTO
from typing import List


def get_user_loans(dto: GetLoans, repo: ILoanRepository) -> List[LoanDTO]:
    with repo:
        result = repo.get_user_loans(dto.user_id)

    response = [LoanDTO(**record.__dict__) for record in result]
    return response
