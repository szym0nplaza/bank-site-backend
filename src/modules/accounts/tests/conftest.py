from modules.accounts.application.interfaces import IClientRepository
from modules.accounts.domain.models import Client, Account, User
from typing import List


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

    def delete_account(self, acc_id: int) -> None:
        if self._accounts.get(acc_id):
            del self._users[acc_id]

    def create_user(self, client: Client) -> None:
        id = next(self.user_id_generator)
        client.user.id = id
        client.accounts[0].user_id = id
        self._accounts
        self._users[id] = {"user": client.user, "accounts": client.accounts}

    def delete_user(self, user_id: int) -> None:
        if self._users.get(user_id):
            del self._users[user_id]
