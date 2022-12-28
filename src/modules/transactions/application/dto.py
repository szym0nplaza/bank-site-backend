from pydantic import BaseModel
from decimal import Decimal


class TransactionAccountDTO(BaseModel):
    currency: str
    number: int
    balance: Decimal
