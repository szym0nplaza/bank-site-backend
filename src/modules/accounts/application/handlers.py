from modules.accounts.application.interfaces import IUserRepository
from modules.accounts.domain.models import User
from modules.accounts.domain.value_objects import Email, Password
from modules.accounts.application import commands


def add_user(dto: commands.CreateUser, repo: IUserRepository):
    user = User(
        name=dto.name,
        surname=dto.surname,
        date_of_birth=dto.date_of_birth,
        login=dto.login,
        email=Email(dto.email),
        password=Password(dto.password),
    )
    with repo:
        repo.create(user)


def update_account(dto: commands.UpdateUser, repo: IUserRepository):
    user = User(
        name=dto.name,
        surname=dto.surname,
        date_of_birth=dto.date_of_birth,
        id=dto.id,
        login=dto.login,
        email=Email(dto.email)
    )
    with repo:
        repo.update(user)


def change_password(dto: commands.ChangePassword, repo: IUserRepository):
    user = User(
        id=dto.id,
        login=dto.login,
        email=Email(dto.email),
        password=Password(dto.password)
    )
    with repo:
        repo.change_password(user)

def delete_user(dto: commands.DeleteUser, repo: IUserRepository):
    with repo:
        repo.delete(dto.id)