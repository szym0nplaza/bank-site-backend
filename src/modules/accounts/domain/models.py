from typing import List, Tuple, Optional, Union
import random
from dataclasses import dataclass

from base.types import Entity
from config.settings import Settings
from cryptography.fernet import Fernet
from modules.accounts.domain.value_objects import (
    Email,
    Password,
    Currency,
    AccountNumber,
)


@dataclass
class User(Entity):
    login: str
    email: Union[Email, str]
    password: Union[Password, str]
    id: Optional[int] = None

    def update_email(self, new_email: Email):
        self.email = new_email

    def change_password(self, new_password: Password):
        self.password = new_password

    def __post_init__(self) -> None:
        self.email = self.email.value
        self.password = self.password.value


@dataclass
class Account(Entity):
    user_id: int
    default_currency: Currency
    number: Optional[AccountNumber] = None
    balance: Optional[float] = None

    def update_balance(self, new_balance: float) -> None:
        self.balance = new_balance

    def change_currency(self, new_currency: Currency) -> None:
        self.default_currency = new_currency

    def __post_init__(self):
        acc_number = random.randint(10**11, 10**12)
        self.number = AccountNumber(acc_number)
        self.balance = round(0, 2)

        self.currency= self.currency.value
        self.number = self.number.value


class Client:
    def __init__(self, data: User, accounts: List[Account]) -> None:
        self.data = data
        self.accounts = accounts

    def get_client_info(self) -> Tuple:
        return self.data, self.accounts

    def check_password(self, db_password: bytes, given_password: str) -> bool:
        return (
            given_password
            == Fernet(Settings.password_key.encode()).decrypt(db_password).decode()
        )
