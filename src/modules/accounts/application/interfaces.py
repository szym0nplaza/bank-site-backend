from abc import abstractmethod, ABC
from modules.accounts.domain.models import User, Client
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

    def __exit__(self, *__args):
        pass

    @abstractmethod
    def list(self) -> List[User]:
        raise NotImplementedError

    @abstractmethod
    def get(self, user_id: int) -> Client:
        """Gets user with assigned accounts"""
        raise NotImplementedError

    @abstractmethod
    def create_user(self, client: Client) -> None:
        """Creates basic user with 1 main account"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, user_id: int) -> None:
        raise NotImplementedError
