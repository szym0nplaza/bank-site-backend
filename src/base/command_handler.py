from modules.accounts.application.commands import (
    UpdateUser,
    CreateUser,
    ChangePassword,
    DeleteUser,
    CreateAccount,
    ChangeCurrency,
    DeleteAccount
)
from modules.accounts.application.handlers import (
    add_user,
    update_user,
    change_password,
    delete_user,
    add_account,
    change_currency,
    delete_account
)
from config.settings import settings
from base.types import Command, Repository
from base.dto import ResponseDTO


USER_COMMAND_HANDLERS = {
    CreateUser: {"handler": add_user, "response_code": 201},
    UpdateUser: {"handler": update_user, "response_code": 200},
    ChangePassword: {"handler": change_password, "response_code": 200},
    DeleteUser: {"handler": delete_user, "response_code": 200},
    CreateAccount: {"handler": add_account, "response_code": 201},
    ChangeCurrency: {"handler": change_currency, "response_code": 200},
    DeleteAccount: {"handler": delete_account, "response_code": 200},
}


COMMAND_HANDLERS = {**USER_COMMAND_HANDLERS}  # Will join all handlers in one


def handle_command(command: Command, repo: Repository) -> ResponseDTO:
    try:
        handler = COMMAND_HANDLERS.get(type(command))
        handler["handler"](command, repo)
        return ResponseDTO(message="ok", status=handler.get("response_code"))
    except Exception as e:
        if settings.debug:
            raise e
        return ResponseDTO(message=str(e), status=500)
