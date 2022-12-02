from base.types import Command
from dataclasses import dataclass
from datetime import date


@dataclass
class CreateUser(Command):
    name: str
    surname: str
    date_of_birth: date
    login: str
    email: str
    password: str


@dataclass
class UpdateUser(Command):
    id: int
    name: str
    surname: str
    date_of_birth: date
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