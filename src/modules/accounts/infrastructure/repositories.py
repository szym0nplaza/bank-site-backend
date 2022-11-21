from modules.accounts.application.interfaces import IUserRepository
from modules.accounts.domain.models import User
from config.settings import DBSession
from sqlalchemy.exc import IntegrityError


class UserRepository(IUserRepository):
    def __init__(self, session=DBSession.get_session()) -> None:
        self._session = session

    def create(self, user: User) -> None:
        try:
            self._session.add(user)
            self._session.commit()
        except IntegrityError:
            raise ValueError("User with given email already exists!")

    def update(self, user: User) -> None:
        user_data = {
            key: value
            for key, value in user.__dict__.items()
            if key not in ["_sa_instance_state", "password"]
        }
        self._session.query(User).filter_by(id=user.id).update(user_data)
        self._session.commit()
