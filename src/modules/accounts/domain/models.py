from typing import List, Tuple, Optional, Union
from decimal import Decimal
import random
from dataclasses import dataclass
from datetime import date
from base.types import Entity, AggregateRoot
from config.settings import settings
from cryptography.fernet import Fernet
from modules.accounts.domain.value_objects import (
    Email,
    Password,
    Currency,
    AccountNumber,
)


@dataclass
class Account(Entity):
    default_currency: Currency
    user_id: Optional[int] = None
    id: Optional[int] = None
    number: Optional[AccountNumber] = None
    balance: Optional[Decimal] = Decimal('0.00')

    def update_balance(self, new_balance: Decimal) -> None:
        self.balance = new_balance

    def change_currency(self, new_currency: Currency):
        self.default_currency = new_currency.value

    def __post_init__(self):
        acc_number = random.randint(10**11, 10**12)
        self.number = AccountNumber(acc_number)

        self.default_currency = self.default_currency.value
        self.number = self.number.value


@dataclass
class User(Entity):
    login: str
    email: Union[Email, str]
    name: str
    surname: str
    date_of_birth: date
    password: Union[Password, str]
    id: Optional[int] = None

    def update_data(self, dto):
        for field in self.__dict__.keys():
            if field in ["_sa_instance_state", "password"]:
                continue

            new_value = getattr(dto, field)
            setattr(self, field, new_value)

    def change_password(self, new_password: Password):
        self.password = new_password.value

    def check_password(self, given_password: str) -> bool:
        return (
            Fernet(settings.password_key.encode()).decrypt(given_password).decode()
            == Fernet(settings.password_key.encode())
            .decrypt(self.password.encode())
            .decode()
        )

    def __post_init__(self) -> None:
        self.email = self.email.value
        if self.password:
            self.password = self.password.value


class Client(AggregateRoot):
    def __init__(self, user: User, accounts: List[Account]) -> None:
        self.user = user
        self.accounts = accounts

    def get_client_info(self) -> Tuple:
        return self.user, self.accounts
