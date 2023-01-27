from modules.loans.application.interfaces import ILoanRepository
from modules.loans.domain.models import Loan


def id_generator():
    id = 1
    while True:
        yield id
        id += 1


class LoanMockRepository(ILoanRepository):
    _loans = dict()
    _id_generator = id_generator()

    def register_loan(self, loan: Loan):
        id = next(self._id_generator)
        loan.id = id
        self._loans[id] = loan

    def get_user_loans(self, user_id: int):
        result = list(filter(lambda record: record.user_id == user_id, self._loans.values()))
        return result
