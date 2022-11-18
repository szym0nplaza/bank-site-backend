from abc import abstractmethod, ABC
from modules.accounts.domain.models import Account, User
from typing import List


class IUserRepository(ABC):
    @abstractmethod
    def list(self) -> List[User]:
        raise NotImplementedError

    @abstractmethod
    def get(self, user_id: int) -> User:
        raise NotImplementedError

    @abstractmethod
    def create(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, user_id: int) -> None:
        raise NotImplementedError
