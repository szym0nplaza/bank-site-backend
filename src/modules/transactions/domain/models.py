from dataclasses import dataclass
from base.types import Entity
from datetime import datetime
from decimal import Decimal


@dataclass
class Transaction(Entity):
    timestamp: datetime
    sender_account: int
    receiver_account: int
    amount: Decimal
    currency: str
    sender_post_balance: Decimal
    receiver_post_balance: Decimal
