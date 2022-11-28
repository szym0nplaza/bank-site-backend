from fastapi import APIRouter
from modules.accounts.application.commands import (
    CreateUser,
    UpdateUser,
    ChangePassword,
    DeleteUser,
)
from modules.accounts.application.queries import GetUserList, GetUser
from modules.accounts.application.dto import UserDTO
from base.command_handler import handle_command
from base.query_handler import handle_query
from typing import List
from modules.accounts.infrastructure.repositories import UserRepository


accounts_router = router = APIRouter()


@router.post("/create-user")
async def create_user(dto: CreateUser):
    response = handle_command(dto, UserRepository())
    return response


@router.patch("/update-user")
async def update_user(dto: UpdateUser):
    response = handle_command(dto, UserRepository())
    return response


@router.patch("/change-password")
async def change_password(dto: ChangePassword):
    response = handle_command(dto, UserRepository())
    return response


@router.delete("/delete-user/{user_id}")
async def delete_user(user_id: int):
    dto = DeleteUser(id=user_id)
    response = handle_command(dto, UserRepository())
    return response


@router.get("/users", response_model=List[UserDTO])
async def get_user_list():
    response = handle_query(GetUserList(), UserRepository())
    return response


@router.get("/users/{user_id}", response_model=UserDTO)
async def get_user(user_id:int):
    dto = GetUser(id=user_id)
    response = handle_query(dto, UserRepository())
    return response
