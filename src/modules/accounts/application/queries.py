from modules.accounts.application.interfaces import AccountQuery
from typing import List
from modules.accounts.domain.models import Account


class GetAccountsList(AccountQuery):
    def run_query(self, user_id: int) -> List[Account]:
        return self.account_repo.list(user_id)


class GetAccount(AccountQuery):
    def run_query(self, acc_id: int) -> Account:
        return self.account_repo.get(acc_id)
