from modules.accounts.application.interfaces import IClientRepository
from modules.accounts.application.queries import queries
from modules.accounts.domain.models import Account
from modules.accounts.application.dto import UserDTO, ClientDTO, AccountDTO
from typing import List


def get_account(dto: queries.GetAccount, repo: IClientRepository) -> AccountDTO:
    with repo:
        account: Account = repo.get_account(dto.id)
        response_data = AccountDTO(**account.__dict__)

    return response_data


def get_account_by_number(dto: queries.GetAccountByNumber, repo: IClientRepository) -> AccountDTO:
    with repo:
        account: Account = repo.get_account(dto.number)
        response_data = AccountDTO(**account.__dict__)

    return response_data


def get_user_list(_dto: queries.GetUserList, repo: IClientRepository) -> List[UserDTO]:
    with repo:
        db_data = repo.get_user_list()
        response_data = [UserDTO(**record.__dict__) for record in db_data]

    return response_data


def get_user(dto: queries.GetUser, repo: IClientRepository) -> ClientDTO:
    with repo:
        client = repo.get_user(dto.id)
        user, accounts = client.get_client_info()
        user = UserDTO(**user.__dict__)
        accounts = [AccountDTO(**acc.__dict__) for acc in accounts]
        response_data = ClientDTO(user=user, accounts=accounts)

    return response_data