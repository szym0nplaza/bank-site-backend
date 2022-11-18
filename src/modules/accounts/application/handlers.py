from modules.accounts.application.interfaces import IUserRepository
from modules.accounts.domain.models import User
from modules.accounts.domain.value_objects import Email, Password
from modules.accounts.application.commands import CreateUser


def add_user(command: CreateUser, repo: IUserRepository):
    user = User(
        login=command.login,
        email=Email(command.email),
        password=Password(command.password),
    )
    repo.create(user)
