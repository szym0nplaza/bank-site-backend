from dataclasses import dataclass
from base.types import Entity
from datetime import datetime
from decimal import Decimal
from typing import Optional


@dataclass
class Transaction(Entity):
    sender_account: int
    receiver_account: int
    amount: Decimal
    currency: Optional[str] = None
    sender_post_balance: Optional[Decimal] = None
    receiver_post_balance: Optional[Decimal] = None
    timestamp: datetime = datetime.now()

    def calculate_post_balances(
        self, sender_current_balance: Decimal, receiver_current_balance: Decimal
    ) -> None:
        self.sender_post_balance = sender_current_balance - self.amount
        self.receiver_post_balance = receiver_current_balance + self.amount

    def check_currency(self, sender_currency: str, receiver_currency: str):
        try:
            assert sender_currency == receiver_currency
            self.currency = sender_currency
        except AssertionError:
            raise AssertionError("Currencies doesn't match!")

    def check_sender_ability(self, sender_account_balance: Decimal):
        try:
            assert sender_account_balance > self.amount
        except AssertionError:
            raise AssertionError("Sender doesn't have enough funds to proceed transaction!")
