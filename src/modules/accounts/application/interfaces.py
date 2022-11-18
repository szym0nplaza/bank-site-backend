from abc import abstractmethod, ABC
from modules.accounts.domain.models import User
from base.types import Repository
from typing import List


class IUserRepository(ABC, Repository):
    def list(self) -> List[User]:
        raise NotImplementedError

    def get(self, user_id: int) -> User:
        raise NotImplementedError

    @abstractmethod
    def create(self, user: User) -> None:
        raise NotImplementedError

    def update(self, user: User) -> None:
        raise NotImplementedError

    def delete(self, user_id: int) -> None:
        raise NotImplementedError
