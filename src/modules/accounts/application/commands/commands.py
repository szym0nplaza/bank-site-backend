from base.types import Command
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class CreateUser(Command):
    name: str
    surname: str
    date_of_birth: str
    login: str
    email: str
    password: str


@dataclass
class CreateAccount(Command):
    default_currency: str
    user_id: int


@dataclass
class DeleteAccount(Command):
    id: int


@dataclass
class ChangeCurrency(Command):
    id: int
    currency: str


@dataclass
class UpdateUser(Command):
    id: int
    name: str
    surname: str
    date_of_birth: str
    login: str
    email: str


@dataclass
class ChangePassword(Command):
    id: int
    new_password: str
    repeated_password: str


@dataclass
class DeleteUser(Command):
    id: int


@dataclass
class UpdateBalance(Command):
    account_number: int
    amount: Decimal