from .commands import RegisterTransaction
from modules.transactions.application.interfaces import ITransactionRepository
from modules.transactions.application.ports import AccountsPort
from modules.transactions.domain.models import Transaction


def add_transaction(dto: RegisterTransaction, repo: ITransactionRepository, **kwargs):
    accounts_client: AccountsPort = kwargs[
        "accounts_client"
    ]  # Using square brackets, err will be handled anyway
    sender_acc, receiver_acc = accounts_client.get_transaction_accounts(
        dto.sender_account_number, dto.receiver_account_number
    )
    transaction = Transaction(
        amount=dto.amount,
        sender_account=dto.sender_account_number,
        receiver_account=dto.receiver_account_number,
    )

    transaction.check_currency(sender_acc.currency, receiver_acc.currency)
    transaction.check_sender_ability(sender_acc.balance)
    transaction.calculate_post_balances(sender_acc.balance, receiver_acc.balance)
    accounts_client.update_accounts_balances(
        dto.sender_account_number,
        dto.receiver_account_number,
        dto.amount,
    )

    repo.create_transaction(transaction)
