from base.types import Query, Repository
from base.dto import ResponseDTO
from config.settings import settings
from .queries_base import QUERY_HANDLERS


# Base handler for queries from all modules
# Ensure that query is registered in queries_base.py file
def handle_query(query: Query, repo: Repository, **kwargs) -> ResponseDTO:
    try:
        handler = QUERY_HANDLERS.get(type(query))
        response_data = handler["handler"](query, repo, **kwargs)
        return response_data
    except Exception as e:
        if settings.debug:
            raise e
        return ResponseDTO(message=str(e), status=500)
