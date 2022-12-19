from fastapi import APIRouter
from fastapi.responses import JSONResponse
from modules.accounts.application.commands.commands import (
    CreateUser,
    UpdateUser,
    ChangePassword,
    DeleteUser,
    CreateAccount
)
from modules.accounts.application.queries.queries import GetUserList, GetUser
from modules.accounts.application.dto import UserDTO, ClientDTO
from base.commands.command_handler import handle_command
from base.queries.query_handler import handle_query
from typing import List
from modules.accounts.infrastructure.repositories import ClientRepository


accounts_router = router = APIRouter()


@router.post("/create-user")
async def create_user(dto: CreateUser):
    response = handle_command(dto, ClientRepository())
    return JSONResponse(response.message, status_code=response.status)

@router.post("/create-account")
async def create_account(dto: CreateAccount):
    response = handle_command(dto, ClientRepository())
    return JSONResponse(response.message, status_code=response.status)


@router.patch("/update-user")
async def update_user(dto: UpdateUser):
    response = handle_command(dto, ClientRepository())
    return JSONResponse(response.message, status_code=response.status)


@router.patch("/change-password")
async def change_password(dto: ChangePassword):
    response = handle_command(dto, ClientRepository())
    return JSONResponse(response.message, status_code=response.status)


@router.delete("/delete-user/{user_id}")
async def delete_user(user_id: int):
    dto = DeleteUser(id=user_id)
    response = handle_command(dto, ClientRepository())
    return JSONResponse(response.message, status_code=response.status)


@router.get("/users", response_model=List[UserDTO])
async def get_user_list():
    response = handle_query(GetUserList(), ClientRepository())
    return response


@router.get("/users/{user_id}", response_model=ClientDTO)
async def get_user(user_id:int):
    dto = GetUser(id=user_id)
    response = handle_query(dto, ClientRepository())
    return response
