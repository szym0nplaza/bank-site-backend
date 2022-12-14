from config.settings import settings
from base.types import Command, Repository
from base.dto import ResponseDTO
from .commands_base import COMMAND_HANDLERS


def handle_command(command: Command, repo: Repository) -> ResponseDTO:
    try:
        handler = COMMAND_HANDLERS.get(type(command))
        handler["handler"](command, repo)
        return ResponseDTO(message="ok", status=handler.get("response_code"))
    except Exception as e:
        if settings.debug:
            raise e
        return ResponseDTO(message=str(e), status=500)
