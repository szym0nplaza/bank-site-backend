from fastapi import APIRouter
from modules.accounts.application.commands import (
    CreateUser,
    UpdateUser,
    ChangePassword,
    DeleteUser,
)
from base.handlers import handle_command
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
