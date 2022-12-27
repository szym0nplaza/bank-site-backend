from dataclasses import dataclass
from base.types import Entity
from decimal import Decimal
from typing import Optional
from .value_objects import LoanStatus
from datetime import date
from dateutil.relativedelta import relativedelta


@dataclass
class Loan(Entity):
    user_id: int
    account_id: int
    borrowed_amount: Decimal
    no_installments: int  # number of installments
    currency: str
    paid_installments: int = 0
    billing_month_day: int = 10
    paid_amount: Decimal = Decimal("0.00")
    status: LoanStatus = LoanStatus.ACTIVE
    id: Optional[int] = None

    def get_next_installment(self) -> Decimal:
        if self.no_installments - self.paid_installments == 1:
            return self.borrowed_amount - self.paid_amount
        amount = round(self.borrowed_amount / self.no_installments, 2)
        return Decimal(amount)

    def change_status(self, new_status: LoanStatus) -> None:
        self.status = new_status

    def get_info(self) -> dict:
        remaining_amount = self.borrowed_amount - self.paid_amount
        remaining_installments = self.no_installments - self.paid_installments
        approx_finish = date.today() + relativedelta(months=+remaining_installments)
        progress_percentage = int((self.paid_amount / self.borrowed_amount)*100)
        return {
            "remaining_amount": remaining_amount,
            "remaining_installments": remaining_installments,
            "approx_finish": approx_finish.strftime("%Y-%m"),
            "progress": progress_percentage
        }
