class ValueObject:
    "Base class for value objects"

    def __eq__(self, other) -> bool:
        return self.value == other.value


class Entity:
    """Base class for Entities"""


class Command:
    """Base class for commands"""