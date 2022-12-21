from config.settings import settings
from base.types import Command, Repository
from base.dto import ResponseDTO
from .commands_base import COMMAND_HANDLERS


# Base handler for commands from all modules
# Ensure that command is registered in commands_base.py file
def handle_command(command: Command, repo: Repository, **kwargs) -> ResponseDTO:
    """
    Base handler for commands from all modules \n
    Ensure that command is registered in commands_base.py file \n
    Use `kwargs` for passing extra arguments such as adapters.
    """
    try:
        handler = COMMAND_HANDLERS.get(type(command))
        handler["handler"](command, repo, **kwargs)
        return ResponseDTO(message="ok", status=handler.get("response_code"))
    except Exception as e:
        if settings.debug:
            raise e
        return ResponseDTO(message=str(e), status=500)
