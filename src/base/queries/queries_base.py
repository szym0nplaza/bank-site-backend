### QUERIES
import modules.accounts.application.queries.queries as user_queries
import modules.transactions.application.queries.queries as transaction_queries
import modules.loans.application.queries.queries as loan_queries


### HANDLERS
import modules.transactions.application.queries.handlers as transaction_handlers
import modules.accounts.application.queries.handlers as user_handlers
import modules.loans.application.queries.handlers as loan_handlers


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

### LOAN MODULE QUERIES
LOAN_QUERY_HANDLERS = {loan_queries.GetLoans: {"handler": loan_handlers.get_user_loans}}


QUERY_HANDLERS = {
    **USER_QUERY_HANDLERS,
    **TRANSACTION_QUERY_HANDLERS,
    **LOAN_QUERY_HANDLERS,
}  # Will join all handlers in one
