from abc import abstractmethod, ABC
from modules.accounts.domain.models import Account
from typing import List


class IAccountRepository(ABC):
    def list(self, user_id: int) -> List[Account]:
        raise NotImplementedError

    def get(self, acc_id: int) -> Account:
        raise NotImplementedError

    def create(self, account: Account) -> None:
        raise NotImplementedError

    def update(self, account: Account) -> None:
        raise NotImplementedError

    def delete(self, account_id: int) -> None:
        raise NotImplementedError


class AccountCommand(ABC):
    def __init__(self, account_repository: IAccountRepository) -> None:
        self.account_repo = account_repository

    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError


class AccountQuery(ABC):
    def __init__(self, account_repository: IAccountRepository) -> None:
        self.account_repo = account_repository

    @abstractmethod
    def run_query(self) -> None:
        raise NotImplementedError
