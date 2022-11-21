from modules.accounts.application.commands import UpdateUser, CreateUser
from modules.accounts.application.handlers import add_user, update_account
from fastapi.responses import JSONResponse
from base.types import Command, Repository


COMMAND_HANDLERS = {
    CreateUser: {"handler": add_user, "response_code": 201},
    UpdateUser: {"handler": update_account, "response_code": 200},
}


def handle_command(command: Command, repo: Repository) -> JSONResponse:
    try:
        handler = COMMAND_HANDLERS.get(type(command))
        handler["handler"](command, repo)
        return JSONResponse({"message": "ok"}, status_code=handler.get('response_code'))
    except Exception as e:
        return JSONResponse(str(e), status_code=500)
