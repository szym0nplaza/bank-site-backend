from src.domain.value_objects import Email, Password
from dataclasses import dataclass
from cryptography.fernet import Fernet
from config.settings import settings


@dataclass
class User:
    login: str
    email: Email
    password: Password

    def check_password(self, given_password: str):
        return (
            given_password
            == Fernet(settings.password_key.encode())
            .decrypt(self.password.password)
            .decode()
        )
