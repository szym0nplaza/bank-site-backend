from modules.accounts.application.interfaces import IClientRepository
from modules.accounts.domain.models import User, Account, Client
from config.settings import DBSession
from typing import List


class ClientRepository(IClientRepository):
    def __init__(self, session_class=DBSession) -> None:
        self._session_class = session_class

    def __enter__(self) -> None:
        self._session = self._session_class.get_session()

    def __exit__(self, *__args):
        try:
            self._session.commit()
        except:
            self._session.rollback()
        finally:
            self._session.rollback()
    
    def get_user_list(self) -> List[User]:
        users = self._session.query(User).all()
        return users

    def get_account(self, account_id: int) -> Account:
        return self._session.query(Account).filter_by(id=account_id).first()

    def get_account_by_number(self, account_number: int) -> Account:
        return self._session.query(Account).filter_by(number=str(account_number)).first()

    def get_user(self, user_id: int) -> Client:
        db_user: User = self._session.query(User).filter_by(id=user_id).first()
        accounts: List[Account] = self._session.query(Account).filter_by(user_id=user_id)
        client: Client = Client(db_user, accounts)
        return client

    def create_account(self, account: Account) -> None:
        self._session.add(account)

    def delete_account(self, acc_id: int) -> None:
        self._session.query(Account).filter_by(id=acc_id).delete()

    def get_account_list(self, user_id: int) -> List[Account]:
        accounts: List[Account] = self._session.query(Account).filter_by(user_id=user_id)
        return accounts

    def create_user(self, client: Client) -> None:
        self._session.add(client.user)
        db_user: User = self._session.query(User).filter_by(email=client.user.email).first()
        client.accounts[0].user_id = db_user.id
        self._session.add(client.accounts[0])

    def delete_user(self, user_id: int) -> None:
        self._session.query(User).filter_by(id=user_id).delete()
