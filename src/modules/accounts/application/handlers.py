from modules.accounts.application.interfaces import IUserRepository
from modules.accounts.domain.models import User
from modules.accounts.domain.value_objects import Email, Password
from modules.accounts.application import commands


def add_user(dto: commands.CreateUser, repo: IUserRepository):
    user = User(
        login=dto.login,
        email=Email(dto.email),
        password=Password(dto.password),
    )
    repo.create(user)


def update_account(dto: commands.UpdateUser, repo: IUserRepository):
    user = User(
        id=dto.id,
        login=dto.login,
        email=Email(dto.email)
    )
    repo.update(user)