from dataclasses import dataclass
from base.types import Query


@dataclass
class GetLoans(Query):
    account_number: int