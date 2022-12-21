import pytest
from modules.accounts.application.interfaces import IClientRepository
from modules.accounts.domain.models import Client, Account, User
from modules.accounts.application.dto import AccountDTO
from modules.accounts.domain.value_objects import Currencies
from typing import List, Union
from decimal import Decimal


@pytest.fixture
def account_fixture():
    return (
        AccountDTO(
            user_id=1,
            default_currency=Currencies.EUR,
            number=123456789012,
            balance=Decimal("1000.00"),
        ),
        AccountDTO(
            user_id=2,
            default_currency=Currencies.EUR,
            number=998765432109,
            balance=Decimal("500.00"),
        ),
    )


def id_generator():
    id = 1
    while True:
        yield id
        id += 1


class MockClientRepository(IClientRepository):
    _users = dict()
    _accounts = dict()
    user_id_generator = id_generator()
    acc_id_generator = id_generator()

    def __enter__(self) -> None:
        pass

    def __exit__(self, *__args):
        pass

    def get_user(self, user_id: int) -> Client:
        data = self._users.get(user_id)
        client: Client = Client(user=data.get("user"), accounts=data.get("accounts"))
        return client

    def get_user_list(self) -> List[User]:
        result = list()
        for record in self._users.values():
            result.append(record.get("user"))
        return result

    def create_account(self, account: Account) -> None:
        id = next(self.acc_id_generator)
        self._accounts[id] = account

    def get_account_list(self, user_id: int) -> List[Account]:
        result: List[Account] = [
            record for record in self._accounts if record.user_id == user_id
        ]
        return result

    def get_account(self, account_id: int) -> Union[Account, None]:
        return self._accounts.get(account_id)

    def get_account_by_number(self, account_number: int) -> Union[Account, None]:
        try:
            acc = list(filter(lambda x: x["number"] == account_number, self._accounts))[
                0
            ]
        except IndexError:
            acc = None
        return acc

    def delete_account(self, acc_id: int) -> None:
        if self._accounts.get(acc_id):
            del self._accounts[acc_id]

    def create_user(self, client: Client) -> None:
        id = next(self.user_id_generator)
        client.user.id = id
        client.accounts[0].user_id = id
        self._users[id] = {"user": client.user, "accounts": client.accounts}

    def delete_user(self, user_id: int) -> None:
        if self._users.get(user_id):
            del self._users[user_id]
