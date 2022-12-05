from modules.accounts.application.interfaces import IClientRepository
from modules.accounts.domain.models import Client, Account, User
from typing import List


def id_generator():
    id = 1
    while True:
        yield id
        id += 1


class MockClientRepository(IClientRepository):
    users = dict()
    id = id_generator()

    def __enter__(self) -> None:
        pass

    def __exit__(self, *__args):
        pass

    def get(self, user_id: int) -> Client:
        data = self.users.get(user_id)
        client: Client = Client(user = data.get("user"), accounts=data.get("accounts"))
        return client

    def list(self) -> List[User]:
        result = list()
        for record in self.users.values():
            result.append(record.get("user"))
        return result

    def create_user(self, client: Client) -> None:
        id = next(self.id)
        client.user.id = id
        client.accounts[0].user_id = id
        self.users[id] = {"user": client.user, "accounts": client.accounts}

    def delete(self, user_id: int) -> None:
        if self.users.get(user_id):
            del self.users[user_id]
