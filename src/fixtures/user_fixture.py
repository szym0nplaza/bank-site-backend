from modules.accounts.domain.models import User, Account
from modules.accounts.domain.value_objects import Password, Email, Currency
from sqlalchemy.exc import IntegrityError
from config.settings import DBSession
from decimal import Decimal
from config.logger import logger


session = DBSession().get_session()

user1 = User(
    name="John",
    surname="Backpack",
    date_of_birth="2000-10-10",
    login="user1234",
    email=Email("test1@bank-app.com"),
    password=Password("zaq1@WSX"),
)
user2 = User(
    name="Daniel",
    surname="Pekov",
    date_of_birth="1990-10-10",
    login="user5678",
    email=Email("test2@bank-app.com"),
    password=Password("ZAQ!2wsx"),
)
account1 = Account(
    default_currency=Currency("USD"), user_id=1, balance=Decimal("5000.00")
)
account2 = Account(
    default_currency=Currency("USD"), user_id=2, balance=Decimal("1000.00")
)

try:
    session.bulk_save_objects([user1, user2])
    session.bulk_save_objects([account1, account2])
    session.commit()
    logger.info("Fixtures uploaded.")
except IntegrityError:
    logger.error("Data already uploaded!")
finally:
    session.close()
