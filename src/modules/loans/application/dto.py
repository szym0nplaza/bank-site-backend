from dataclasses import dataclass
from decimal import Decimal


@dataclass
class LoanDTO:
    user_id: int
    account_number: int
    borrowed_amount: Decimal
    no_installments: int
    paid_installments: int 
    paid_amount: Decimal
    billing_month_day: int
    status: str
    currency: str
    id: int