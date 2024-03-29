class ValueObject:
    "Base class for value objects"

    def __eq__(self, other) -> bool:
        return self.value == other.value


class Entity:
    """Base class for Entities"""


class Command:
    """Base class for Commands"""


class Repository:
    """Base class for Repos"""


class Query:
    """Base class for Queries"""


class AggregateRoot:
    """Base aggregate root class"""


class Facade:
    """Base class for facade - module for exposing data from given module to other"""
