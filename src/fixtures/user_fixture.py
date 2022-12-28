from modules.accounts.domain.models import User, Account
from modules.accounts.domain.value_objects import Password, Email, Currency
from sqlalchemy.exc import IntegrityError
from config.settings import DBSession
from decimal import Decimal
from config.logger import logger


session = DBSession().get_session()

user1 = User(
    id=1,
    name="John",
    surname="Backpack",
    date_of_birth="2000-10-10",
    login="user1234",
    email=Email("test1@bank-app.com"),
    password=Password("zaq1@WSX"),
)
user2 = User(
    id=2,
    name="Daniel",
    surname="Pekov",
    date_of_birth="1990-10-10",
    login="user5678",
    email=Email("test2@bank-app.com"),
    password=Password("ZAQ!2wsx"),
)
user3 = User(
    id=3,
    name="Central Bank Account",
    surname="",
    date_of_birth="1971-12-23",
    login="bankadmin1",
    email=Email("bank.admin@bank-app.com"),
    password=Password("@dm1N098"),
)

account1 = Account(
    default_currency=Currency("USD"), user_id=1, balance=Decimal("5000.00")
)
account2 = Account(
    default_currency=Currency("USD"), user_id=2, balance=Decimal("1000.00")
)
account3 = Account(
    default_currency=Currency("USD"), user_id=3, balance=Decimal("99999999.00")
)
account4 = Account(
    default_currency=Currency("EUR"), user_id=3, balance=Decimal("99999999.00")
)
account5 = Account(
    default_currency=Currency("PLN"), user_id=3, balance=Decimal("99999999.00")
)

try:
    session.query(User).delete()
    session.query(Account).delete()
    session.commit()
    session.bulk_save_objects([user1, user2, user3])
    session.bulk_save_objects([account1, account2, account3, account4, account5])
    session.commit()
    logger.info("Fixtures uploaded.")
except IntegrityError:
    logger.error("Data already uploaded!")
finally:
    session.close()
