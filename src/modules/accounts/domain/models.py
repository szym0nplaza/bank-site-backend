from dataclasses import dataclass
from decimal import Decimal
from typing import List

from config.settings import Settings
from cryptography.fernet import Fernet
from modules.accounts.domain.value_objects import Email, Password


@dataclass
class User:
    id: int
    login: str
    email: Email
    password: Password


@dataclass
class Account:
    user_id: int
    number: int
    balance: Decimal

    def __post_init__(self):
        if len(str(self.number)) != 12:
            raise ValueError("Account number must contain 12 digits!")


class Client:
    def __init__(self, data: User, accounts: List[Account]) -> None:
        self.data = data
        self.accounts = accounts

    def check_password(self, db_password: bytes, given_password: str) -> bool:
        return (
            given_password
            == Fernet(Settings.password_key.encode()).decrypt(db_password).decode()
        )
