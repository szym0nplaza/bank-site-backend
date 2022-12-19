from dataclasses import dataclass
from base.types import Command
from decimal import Decimal


@dataclass
class AddTransaction(Command):
    sender_account: int
    receiver_account: int
    amount: Decimal
