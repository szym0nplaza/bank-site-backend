from dataclasses import dataclass
from base.types import Query


@dataclass
class GetTransactionsByAccount(Query):
    account_number: int