from dataclasses import dataclass
from base.types import Query


@dataclass
class GetLoans(Query):
    user_id: int