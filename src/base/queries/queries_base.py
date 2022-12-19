from modules.accounts.application.queries.queries import (
    GetUserList,
    GetUser,
    GetAccount,
    GetAccountByNumber,
)
from modules.accounts.application.queries.handlers import (
    get_user_list,
    get_user,
    get_account,
    get_account_by_number,
)


### ACCOUNTS/USER MODULE QUERIES
USER_QUERY_HANDLERS = {
    GetUserList: {"handler": get_user_list},
    GetUser: {"handler": get_user},
    GetAccount: {"handler": get_account},
    GetAccountByNumber: {"handler": get_account_by_number},
}


QUERY_HANDLERS = {**USER_QUERY_HANDLERS} # Will join all handlers in one
