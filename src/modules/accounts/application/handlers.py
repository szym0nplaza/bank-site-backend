from modules.accounts.application.interfaces import IClientRepository
from modules.accounts.domain.models import User, Account, Client
from modules.accounts.domain.value_objects import Email, Password, Currency
from modules.accounts.application import commands, queries
from modules.accounts.application.dto import UserDTO, ClientDTO, AccountDTO
from typing import List


def add_user(dto: commands.CreateUser, repo: IClientRepository) -> None:
    with repo:
        user = User(
            name=dto.name,
            surname=dto.surname,
            date_of_birth=dto.date_of_birth,
            login=dto.login,
            email=Email(dto.email),
            password=Password(dto.password),
        )

        account = Account(default_currency=Currency("PLN"))
        client = Client(user, [account])
        repo.create_user(client)


def update_user(dto: commands.UpdateUser, repo: IClientRepository) -> None:
    with repo:
        user: User = repo.get(dto.id).user
        user.update_data(dto)


def change_password(dto: commands.ChangePassword, repo: IClientRepository) -> None:
    if not dto.new_password == dto.repeated_password:
        raise AssertionError("Passwords don't match!")

    with repo:
        user: User = repo.get(dto.id).user
        if user.check_password(Password(dto.new_password).value):
            raise ValueError("Passwords are the same!")
        user.change_password(Password(dto.new_password))


def delete_user(dto: commands.DeleteUser, repo: IClientRepository) -> None:
    with repo:
        repo.delete(dto.id)


def get_user_list(_dto: queries.GetUserList, repo: IClientRepository) -> List[UserDTO]:
    with repo:
        db_data = repo.list()
        response_data = [UserDTO(**record.__dict__) for record in db_data]

    return response_data


def get_user(dto: queries.GetUser, repo: IClientRepository) -> ClientDTO:
    with repo:
        client = repo.get(dto.id)
        user, accounts = client.get_client_info()
        user = UserDTO(**user.__dict__)
        accounts = [AccountDTO(**acc.__dict__) for acc in accounts]
        response_data = ClientDTO(user=user, accounts=accounts)

    return response_data
