from abc import abstractmethod, ABC


class IAccountService(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError


class IAccountInputBoundary(ABC):
    pass
