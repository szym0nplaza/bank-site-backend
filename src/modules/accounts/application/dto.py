from datetime import date
from typing import List
from pydantic import BaseModel
from decimal import Decimal
from modules.accounts.domain.value_objects import Currencies


class UserDTO(BaseModel):
    id: int
    name: str
    surname: str
    date_of_birth: date
    email: str
    login: str


class AccountDTO(BaseModel):
    user_id: int
    default_currency: Currencies
    number: int
    balance: Decimal


class ClientDTO(BaseModel):
    user: UserDTO
    accounts: List[AccountDTO]