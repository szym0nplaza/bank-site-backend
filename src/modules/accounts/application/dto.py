from dataclasses import dataclass


@dataclass
class AccountDTO:
    user_id: int
    number: int
    default_currency: str