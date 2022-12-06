from base.command_handler import handle_command
from base.query_handler import handle_query
from .conftest import MockClientRepository
from modules.accounts.application.dto import ClientDTO, UserDTO
from modules.accounts.application.commands import (
    CreateUser,
    UpdateUser,
    DeleteUser,
    CreateAccount,
    ChangeCurrency,
    DeleteAccount
)
from modules.accounts.application.queries import GetUser, GetUserList, GetAccount
from datetime import date


class TestClientOperations:
    repo = MockClientRepository()

    def test_user_add(self):
        handle_command(
            CreateUser(
                name="Name1",
                surname="Test1",
                date_of_birth="2000-10-30",
                login="NameTest1234",
                email="test@mail.com",
                password="zaq1@WSX",
            ),
            self.repo,
        )
        handle_command(
            CreateUser(
                name="Name2",
                surname="Test2",
                date_of_birth="1990-10-30",
                login="NameTest5678",
                email="test2@mail.com",
                password="XSW@1qaz",
            ),
            self.repo,
        )

    def test_get(self):
        result1 = handle_query(GetUser(id=1), self.repo)
        assert isinstance(result1, ClientDTO)
        assert isinstance(result1.user.date_of_birth, date)
        assert len(result1.accounts) == 1
        assert result1.user.name == "Name1"

        result2 = handle_query(GetUser(id=2), self.repo)
        assert isinstance(result2, ClientDTO)
        assert isinstance(result2.user.date_of_birth, date)
        assert len(result2.accounts) == 1
        assert result2.user.name == "Name2"

    def test_user_list(self):
        result = handle_query(GetUserList(), self.repo)
        assert len(result) == 2
        assert isinstance(result[0], UserDTO)
        assert isinstance(result[1], UserDTO)

    def test_update_user(self):
        handle_command(
            UpdateUser(
                id=1,
                name="Changed Name",
                surname="Changed Surname",
                date_of_birth="1997-11-15",
                login="MockUpdate123",
                email="test.change@mail.com",
            ),
            self.repo,
        )
        result = handle_query(GetUser(id=1), self.repo)
        assert result.user.email == "test.change@mail.com"
        assert result.user.name == "Changed Name"
        assert result.user.surname == "Changed Surname"
        assert result.user.date_of_birth == date(1997, 11, 15)
        assert result.user.login == "MockUpdate123"

    def test_user_delete(self):
        handle_command(DeleteUser(id=2), self.repo)
        try:
            handle_query(GetUser(id=2), self.repo)
            assert False
        except AttributeError:
            assert True

    def test_account_add(self):
        handle_command(CreateAccount(user_id=1, default_currency="EUR"), self.repo)

    def test_change_currency(self):
        result_before = handle_query(GetAccount(id=1), self.repo)
        assert result_before.default_currency.value == "EUR"

        handle_command(ChangeCurrency(id=1, currency="PLN"), self.repo)
        result_after = handle_query(GetAccount(id=1), self.repo)
        assert result_after.default_currency.value == "PLN"

    def test_delete_account(self):
        handle_command(DeleteAccount(id=1), self.repo)
        try:
            handle_query(GetAccount(id=1), self.repo)
            assert False
        except AttributeError:
            assert True