from base.types import Query
from dataclasses import dataclass


@dataclass
class GetUserList(Query):
    pass


@dataclass
class GetUser(Query):
    id: int


@dataclass
class GetAccount(Query):
    id: int


@dataclass
class GetAccountByNumber(Query):
    number: int


@dataclass
class GetTransactionAccounts(Query):
    sender_acc_number: int
    receiver_acc_number: int
