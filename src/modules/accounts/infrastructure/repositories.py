from modules.accounts.application.interfaces import IUserRepository
from modules.accounts.domain.models import User
from config.settings import DBSession
from sqlalchemy.exc import IntegrityError
from typing import List


class UserRepository(IUserRepository):
    def __init__(self, session_class=DBSession) -> None:
        self._session_class = session_class

    def __enter__(self) -> None:
        self._session = self._session_class.get_session()

    def __exit__(self, *__args):
        self._session.commit()
    
    def list(self) -> List[User]:
        users = self._session.query(User).all()
        return users

    def get(self, user_id: int) -> User:
        db_user = self._session.query(User).filter_by(id=user_id).first()
        return db_user

    def create(self, user: User) -> None:
        try:
            self._session.add(user)
        except IntegrityError:
            raise ValueError("User with given email already exists!")

    def update(self, user: User) -> None:
        db_user = self._session.query(User).filter_by(id=user.id).first()
        db_user.update_data(user)

    def change_password(self, user: User):
        db_user: User = self._session.query(User).filter_by(id=user.id).first()
        if db_user.check_password(user.password):
            raise ValueError("Passwords are the same!")
        db_user.change_password(user.password)

    def delete(self, user_id: int) -> None:
        self._session.query(User).filter_by(id=user_id).delete()
