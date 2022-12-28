from dataclasses import dataclass
from base.types import Command
from decimal import Decimal


@dataclass
class RegisterLoan(Command):
    user_id: int
    account_number: int
    borrowed_amount: Decimal
    no_installments: int