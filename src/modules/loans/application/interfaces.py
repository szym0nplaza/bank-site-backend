from abc import ABC, abstractmethod
from modules.loans.domain.models import Loan
from base.types import Repository


class ILoanRepository(ABC, Repository):
    def __enter__(self) -> None:
        pass

    def __exit__(self, *__args) -> None:
        pass
    
    @abstractmethod
    def register_loan(self, loan: Loan):
        raise NotImplementedError

    @abstractmethod
    def get_user_loans(self, user_id: int):
        raise NotImplementedError
