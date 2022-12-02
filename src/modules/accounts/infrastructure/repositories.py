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
    
    def list(self) -> List[User]:
        users = self._session.query(User).all()
        return users

    def get(self, user_id: int) -> Client:
        db_user: User = self._session.query(User).filter_by(id=user_id).first()
        accounts: List[Account] = self._session.query(Account).filter_by(user_id=user_id)
        client: Client = Client(db_user, accounts)
        return client

    def create_user(self, client: Client) -> None:
        self._session.add(client.user)
        db_user: User = self._session.query(User).filter_by(email=client.user.email).first()
        client.accounts[0].user_id = db_user.id
        self._session.add(client.accounts[0])

    def delete(self, user_id: int) -> None:
        self._session.query(User).filter_by(id=user_id).delete()
