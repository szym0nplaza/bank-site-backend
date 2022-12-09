from abc import abstractmethod, ABC
from modules.accounts.domain.models import User, Client, Account
from base.types import Repository
from typing import List


class IClientRepository(ABC, Repository):
    """
    Interface for user DB operations.
    Use as:
    ```
    repo = UserRepositoryImplementation()
    with repo:
        do operations
    ```
    """

    def __enter__(self, session) -> None:
        pass

    def __exit__(self, *__args) -> None:
        pass

    @abstractmethod
    def get_user_list(self) -> List[User]:
        raise NotImplementedError

    @abstractmethod
    def get_user(self, user_id: int) -> Client:
        """Gets user with assigned accounts"""
        raise NotImplementedError

    @abstractmethod
    def get_account(self, account_id: int) -> Account:
        """Gets user with assigned accounts"""
        raise NotImplementedError

    @abstractmethod
    def get_account_by_number(self, account_number: int) -> Account:
        """Gets user with assigned accounts"""
        raise NotImplementedError

    @abstractmethod
    def create_account(self, account: Account) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete_account(self, acc_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_account_list(self, user_id: int) -> List[Account]:
        raise NotImplementedError

    @abstractmethod
    def create_user(self, client: Client) -> None:
        """Creates basic user with 1 main account"""
        raise NotImplementedError

    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        raise NotImplementedError
