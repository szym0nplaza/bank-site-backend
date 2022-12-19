from dataclasses import dataclass
from decimal import Decimal


@dataclass
class TransactionAccountDTO:
    currency: str
    number: int
    balance: Decimal
