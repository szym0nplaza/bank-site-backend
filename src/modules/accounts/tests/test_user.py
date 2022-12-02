import pytest
from base.command_handler import handle_command
from base.query_handler import handle_query
from .conftest import MockUserRepository
from modules.accounts.application.dto import ClientDTO, UserDTO
from modules.accounts.application.commands import CreateUser
from modules.accounts.application.queries import GetUser, GetUserList
from datetime import date


class TestUserOperations:
    repo = MockUserRepository()

    def test_add(self):
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

    def test_list(self):
        result = handle_query(GetUserList(), self.repo)
        assert len(result) == 2
        assert isinstance(result[0], UserDTO)
        assert isinstance(result[1], UserDTO)
