from modules.accounts.application.interfaces import IUserRepository
from modules.accounts.domain.models import User
from modules.accounts.domain.value_objects import Email, Password
from modules.accounts.application import commands, queries
from modules.accounts.application.dto import UserDTO
from typing import List


def add_user(dto: commands.CreateUser, repo: IUserRepository) -> None:
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


def update_account(dto: commands.UpdateUser, repo: IUserRepository) -> None:
    user = User(
        name=dto.name,
        surname=dto.surname,
        date_of_birth=dto.date_of_birth,
        id=dto.id,
        login=dto.login,
        email=Email(dto.email),
    )
    with repo:
        repo.update(user)


def change_password(dto: commands.ChangePassword, repo: IUserRepository) -> None:
    user = User(
        id=dto.id,
        login=dto.login,
        email=Email(dto.email),
        password=Password(dto.new_password),
    )

    repeated_password = Password(dto.repeated_password).value
    if not user.check_password(repeated_password):
        raise AssertionError("Passwords don't match!")

    with repo:
        repo.change_password(user)


def delete_user(dto: commands.DeleteUser, repo: IUserRepository) -> None:
    with repo:
        repo.delete(dto.id)


def get_user_list(_dto: queries.GetUserList, repo: IUserRepository) -> List[UserDTO]:
    with repo:
        db_data = repo.list()
        response_data = [UserDTO(**record.__dict__) for record in db_data]

    return response_data


def get_user(dto: queries.GetUser, repo: IUserRepository) -> UserDTO:
    with repo:
        db_data = repo.get(dto.id).__dict__
        response_data = UserDTO(**db_data)

    return response_data
