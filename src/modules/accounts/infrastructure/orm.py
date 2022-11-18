from config.settings import DBSession
from modules.accounts.domain import models, value_objects
from sqlalchemy import Column, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import mapper


class User(DBSession.base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    login = Column(String)
    email = Column(String)
    password = Column(String)


class Account(DBSession.base):
    __tablename__ = "accounts"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    default_currency = Column(Enum(value_objects.Currencies))
    number = Column(Integer)
    balance = Column(Float)


mapper(models.User, User)
mapper(models.Account, Account)
