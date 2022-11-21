from base.types import Command
from dataclasses import dataclass


@dataclass
class CreateUser(Command):
    login: str
    email: str
    password: str


@dataclass
class UpdateUser(Command):
    id: int
    login: str
    email: str

