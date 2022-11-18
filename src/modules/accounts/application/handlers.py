from modules.accounts.application.interfaces import IUserRepository
from modules.accounts.domain.models import User
from modules.accounts.domain.value_objects import Email, Password
from modules.accounts.application.commands import CreateUser


def add_user(command: CreateUser, repo: IUserRepository):
    user = User(
        login=command.login,
        email=Email(command.email),
        password=Password(command.password),
    )
    repo.create(user)


COMMAND_HANDLERS = {CreateUser: add_user}


def handle_command(command, repo):
    try:
        handler = COMMAND_HANDLERS[type(command)]
        handler(command, repo)
    except Exception as e:
        raise RuntimeError(e)
