import modules.accounts.application.queries.queries as user_queries
import modules.accounts.application.queries.handlers as user_handlers

### ACCOUNTS/USER MODULE QUERIES
USER_QUERY_HANDLERS = {
    user_queries.GetUserList: {"handler": user_handlers.get_user_list},
    user_queries.GetUser: {"handler": user_handlers.get_user},
    user_queries.GetAccount: {"handler": user_handlers.get_account},
    user_queries.GetAccountByNumber: {"handler": user_handlers.get_account_by_number},
    user_queries.GetTransactionAccounts: {"handler": user_handlers.get_transaction_accounts}
}


QUERY_HANDLERS = {**USER_QUERY_HANDLERS} # Will join all handlers in one
