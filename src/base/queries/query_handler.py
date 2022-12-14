from base.types import Query, Repository
from base.dto import ResponseDTO
from config.settings import settings
from .queries_base import QUERY_HANDLERS


def handle_query(query: Query, repo: Repository) -> ResponseDTO:
    try:
        handler = QUERY_HANDLERS.get(type(query))
        response_data = handler["handler"](query, repo)
        return response_data
    except Exception as e:
        if settings.debug:
            raise e
        return ResponseDTO(message=str(e), status=500)
