import re
from typing import Union

from config.settings import Settings
from cryptography.fernet import Fernet
from dataclasses import dataclass

EMAIL_REGEX = r"^\S+@\S+\.\S+"
PASSWORD_REGEX = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}"


@dataclass(frozen=True)
class Email:
    value: str

    def __post_init__(self) -> None:
        if not re.match(EMAIL_REGEX, self.value):
            raise ValueError("Provided value does not match any email pattern!")

    def __str__(self) -> str:
        return self.value


@dataclass
class Password:
    value: Union[str, bytes]

    def __post_init__(self) -> None:
        if not re.match(PASSWORD_REGEX, self.value):
            raise ValueError(
                "Password must contain at least 8 characters,\
                1 letter, 1 number and 1 special character!"
            )
        self.value = Fernet(Settings.password_key.encode()).encrypt(self.value.encode())
