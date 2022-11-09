from modules.accounts.application.interfaces import AccountCommand
from modules.accounts.application.dto import AccountDTO
from modules.accounts.domain.models import Account


class CreateAccount(AccountCommand):
    def execute(self, acc_info: AccountDTO) -> None:
        account = Account(**(acc_info.__dict__))
        self.account_repo.create(account)


class UpdateAccount(AccountCommand):
    def execute(self, acc_info: AccountDTO) -> None:
        self.account_repo.update(Account(**acc_info.__dict__))


class DeleteAccount(AccountCommand):
    def execute(self, acc_id: int) -> None:
        self.account_repo.delete(acc_id)
