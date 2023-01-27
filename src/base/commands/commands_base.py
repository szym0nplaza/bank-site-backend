### COMMANDS
from modules.accounts.application.commands import commands as user_commands
from modules.transactions.application.commands import commands as transaction_commands
from modules.loans.application.commands import commands as loan_commands


### HANDLERS
from modules.accounts.application.commands import handlers as user_handlers
from modules.transactions.application.commands import handlers as transaction_handlers
from modules.loans.application.commands import handlers as loan_handlers


### ACCOUNTS/USER MODULE COMMANDS
USER_COMMAND_HANDLERS = {
    user_commands.CreateUser: {"handler": user_handlers.add_user, "response_code": 201},
    user_commands.UpdateUser: {
        "handler": user_handlers.update_user,
        "response_code": 200,
    },
    user_commands.ChangePassword: {
        "handler": user_handlers.change_password,
        "response_code": 200,
    },
    user_commands.DeleteUser: {
        "handler": user_handlers.delete_user,
        "response_code": 200,
    },
    user_commands.CreateAccount: {
        "handler": user_handlers.add_account,
        "response_code": 201,
    },
    user_commands.ChangeCurrency: {
        "handler": user_handlers.change_currency,
        "response_code": 200,
    },
    user_commands.DeleteAccount: {
        "handler": user_handlers.delete_account,
        "response_code": 200,
    },
    user_commands.UpdateBalance: {
        "handler": user_handlers.update_account_balance,
        "response_code": 200,
    },
}

### TRANSACTIONS MODULE COMMANDS
TRANSACTION_COMMAND_HANDLERS = {
    transaction_commands.RegisterTransaction: {
        "handler": transaction_handlers.add_transaction,
        "response_code": 201,
    }
}

###
LOAN_COMMAND_HANDLERS = {
    loan_commands.RegisterLoan: {
    "handler": loan_handlers.add_loan,
    "response_code": 201,
    }
}


COMMAND_HANDLERS = {
    **USER_COMMAND_HANDLERS,
    **TRANSACTION_COMMAND_HANDLERS,
    **LOAN_COMMAND_HANDLERS
}  # Will join all handlers in one
