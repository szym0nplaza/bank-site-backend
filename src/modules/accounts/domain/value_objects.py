import re
from typing import Union
from dataclasses import dataclass
import enum

from base.types import ValueObject
from config.settings import settings
from cryptography.fernet import Fernet


EMAIL_REGEX = r"^\S+@\S+\.\S+"
PASSWORD_REGEX = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}"


class Currencies(enum.Enum):
    pln = "PLN"
    usd = "USD"
    eur = "EUR"

    def __str__(self):
        return str(self.value)


@dataclass
class Email(ValueObject):
    value: str

    def __post_init__(self) -> None:
        if not re.match(EMAIL_REGEX, self.value):
            raise ValueError("Provided value does not match any email pattern!")

    def __str__(self) -> str:
        return self.value


@dataclass
class Password(ValueObject):
    value: Union[str, bytes]

    def __post_init__(self) -> None:
        if not re.match(PASSWORD_REGEX, self.value):
            raise ValueError(
                "Password must contain at least 8 characters,\
                1 letter, 1 number and 1 special character!"
            )
        self.value = Fernet(settings.password_key.encode()).encrypt(self.value.encode()).decode()


@dataclass
class Currency(ValueObject):
    """
    Default currency value object.
    Value must be PLN, USD or EUR.
    """

    value: str

    def __post_init__(self) -> None:
        acceptable_currencies = [item.value for item in list(Currencies)]
        if len(self.value) != 3 and self.value not in acceptable_currencies:
            raise ValueError(
                "Incorrect currency string! Choose one from: PLN, USD, EUR."
            )


@dataclass
class AccountNumber(ValueObject):
    value: str

    def __post_init__(self):
        if len(str(self.value)) != 12:
            raise ValueError("Account number must contain 12 digits!")
