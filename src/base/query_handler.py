from modules.accounts.application.queries import GetUserList, GetUser
from modules.accounts.application.handlers import get_user_list, get_user
from base.types import Query, Repository
from fastapi.responses import JSONResponse
from config.settings import settings


USER_QUERY_HANDLERS = {
    GetUserList: {"handler": get_user_list},
    GetUser: {"handler": get_user},
}


QUERY_HANDLERS = {**USER_QUERY_HANDLERS}


def handle_query(query: Query, repo: Repository) -> JSONResponse:
    try:
        handler = QUERY_HANDLERS.get(type(query))
        response_data = handler["handler"](query, repo)
        return response_data
    except Exception as e:
        if settings.debug:
            raise e
        return JSONResponse(str(e), status_code=500)
