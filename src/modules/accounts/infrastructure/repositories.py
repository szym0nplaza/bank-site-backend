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
        user = self._session.query(User).filter_by(id=user_id).first()
        return user

    def create(self, user: User) -> None:
        try:
            self._session.add(user)
        except IntegrityError:
            raise ValueError("User with given email already exists!")

    def update(self, user: User) -> None:
        user_data = {
            key: value
            for key, value in user.__dict__.items()
            if key not in ["_sa_instance_state", "password"]
        }
        self._session.query(User).filter_by(id=user.id).update(user_data)

    def change_password(self, dto: User):
        user: User = self._session.query(User).filter_by(id=dto.id).first()
        if user.check_password(dto.password):
            raise ValueError("Passwords are the same!")
        user.password = dto.password

    def delete(self, user_id: int) -> None:
        self._session.query(User).filter_by(id=user_id).delete()
