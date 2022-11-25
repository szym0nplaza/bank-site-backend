from modules.accounts.application.commands import UpdateUser, CreateUser, ChangePassword, DeleteUser
from modules.accounts.application.handlers import (
    add_user,
    update_account,
    change_password,
    delete_user
)
from config.settings import settings
from fastapi.responses import JSONResponse
from base.types import Command, Repository


USER_COMMAND_HANDLERS = {
    CreateUser: {"handler": add_user, "response_code": 201},
    UpdateUser: {"handler": update_account, "response_code": 200},
    ChangePassword: {"handler": change_password, "response_code": 200},
    DeleteUser: {"handler": delete_user, "response_code": 200},
}


COMMAND_HANDLERS = {**USER_COMMAND_HANDLERS} # Will join all handlers in one


def handle_command(command: Command, repo: Repository) -> JSONResponse:
    try:
        handler = COMMAND_HANDLERS.get(type(command))
        handler["handler"](command, repo)
        return JSONResponse({"message": "ok"}, status_code=handler.get("response_code"))
    except Exception as e:
        if settings.debug:
            raise e
        return JSONResponse(str(e), status_code=500)
