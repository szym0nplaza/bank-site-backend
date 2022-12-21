from dataclasses import dataclass
from base.types import Command
from decimal import Decimal


@dataclass
class RegisterTransaction(Command):
    sender_account_number: int
    receiver_account_number: int
    amount: Decimal
