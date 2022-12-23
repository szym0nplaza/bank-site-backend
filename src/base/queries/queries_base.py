### QUERIES
import modules.accounts.application.queries.queries as user_queries
import modules.accounts.application.queries.handlers as user_handlers


### HANDLERS
import modules.transactions.application.queries.handlers as transaction_handlers
import modules.transactions.application.queries.queries as transaction_queries


### ACCOUNTS/USER MODULE QUERIES
USER_QUERY_HANDLERS = {
    user_queries.GetUserList: {"handler": user_handlers.get_user_list},
    user_queries.GetUser: {"handler": user_handlers.get_user},
    user_queries.GetAccount: {"handler": user_handlers.get_account},
    user_queries.GetAccountByNumber: {"handler": user_handlers.get_account_by_number},
    user_queries.GetTransactionAccounts: {
        "handler": user_handlers.get_transaction_accounts
    },
}

### TRANSACTION MODULE QUERIES
TRANSACTION_QUERY_HANDLERS = {
    transaction_queries.GetTransactionsByAccount: {
        "handler": transaction_handlers.get_transactions
    }
}


QUERY_HANDLERS = {**USER_QUERY_HANDLERS, **TRANSACTION_QUERY_HANDLERS}  # Will join all handlers in one
