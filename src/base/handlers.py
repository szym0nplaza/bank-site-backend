from modules.accounts.application.commands import CreateUser
from modules.accounts.application.handlers import add_user
from base.types import Command, Repository


COMMAND_HANDLERS = {CreateUser: add_user}


def handle_command(command: Command, repo: Repository):
    try:
        handler = COMMAND_HANDLERS[type(command)]
        handler(command, repo)
    except Exception as e:
        raise RuntimeError(e)
