from modules.accounts.application.interfaces import AccountQuery
from typing import List
from modules.accounts.domain.models import Account


class GetAccountsList(AccountQuery):
    def run_query(self) -> List[Account]:
        return self.account_repo.list()


class GetAccount(AccountQuery):
    def run_query(self, acc_id: int) -> Account:
        return self.account_repo.get(acc_id)
