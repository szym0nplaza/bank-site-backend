import re
from cryptography.fernet import Fernet
from config.settings import settings


EMAIL_REGEX = r"^\S+@\S+\.\S+"
PASSWORD_REGEX = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}"


class Email:
    def __init__(self, email: str) -> None:
        if not re.match(EMAIL_REGEX, email):
            raise ValueError("Provided value does not match any email pattern!")
        self.email = email

    def __str__(self) -> str:
        return self.email


class Password:
    def __init__(self, password: str) -> None:
        if not re.match(PASSWORD_REGEX, password):
            raise ValueError(
                "Password must contain at least 8 characters,\
                1 letter, 1 number and 1 special character!"
            )
        self.password = Fernet(settings.password_key.encode()).encrypt(
            password.encode()
        )
