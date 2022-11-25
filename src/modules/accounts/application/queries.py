from base.types import Query
from dataclasses import dataclass


@dataclass
class GetUserList(Query):
    pass


@dataclass
class GetUser(Query):
    id: int
