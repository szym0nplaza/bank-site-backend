from modules.accounts.application.interfaces import IClientRepository
from modules.accounts.domain.models import User, Account, Client
from modules.accounts.domain.value_objects import Email, Password, Currency
from modules.accounts.application.commands import commands
from decimal import Decimal


def add_user(dto: commands.CreateUser, repo: IClientRepository, **_kwargs) -> None:
    with repo:
        user = User(
            name=dto.name,
            surname=dto.surname,
            date_of_birth=dto.date_of_birth,
            login=dto.login,
            email=Email(dto.email),
            password=Password(dto.password),
        )

        while True:
            # Temporary solution for generating unique acc numbers
            account = Account(default_currency=Currency("PLN"))
            if not repo.get_account_by_number(account.number):
                break

        client = Client(user, [account])
        repo.create_user(client)


def add_account(dto: commands.CreateAccount, repo: IClientRepository, **_kwargs):
    with repo:
        account = Account(
            user_id=dto.user_id, default_currency=Currency(dto.default_currency)
        )
        repo.create_account(account)


def update_user(dto: commands.UpdateUser, repo: IClientRepository, **_kwargs) -> None:
    with repo:
        user: User = repo.get_user(dto.id).user
        user.update_data(dto)


def change_password(dto: commands.ChangePassword, repo: IClientRepository) -> None:
    if not dto.new_password == dto.repeated_password:
        raise AssertionError("Passwords don't match!")

    with repo:
        user: User = repo.get_user(dto.id).user
        if user.check_password(Password(dto.new_password).value):
            raise ValueError("Passwords are the same!")
        user.change_password(Password(dto.new_password))


def delete_user(dto: commands.DeleteUser, repo: IClientRepository, **_kwargs) -> None:
    with repo:
        repo.delete_user(dto.id)


def change_currency(dto: commands.ChangeCurrency, repo: IClientRepository, **_kwargs) -> None:
    with repo:
        account: Account = repo.get_account(dto.id)
        account.change_currency(Currency(dto.currency))


def delete_account(dto: commands.DeleteAccount, repo: IClientRepository, **_kwargs) -> None:
    with repo:
        repo.delete_account(dto.id)


def update_account_balance(dto: commands.UpdateBalance, repo: IClientRepository, **_kwargs) -> None:
    with repo:
        account: Account = repo.get_account_by_number(dto.account_number)
        account.update_balance(Decimal(account.balance)+dto.amount)