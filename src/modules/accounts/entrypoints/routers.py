from fastapi import APIRouter
from fastapi.responses import JSONResponse
from modules.accounts.application.commands import CreateUser, UpdateUser
from base.handlers import handle_command
from modules.accounts.infrastructure.repositories import UserRepository
from config.settings import DBSession


accounts_router = router = APIRouter()


@router.post("/create-user")
async def create_user(user: CreateUser):
    response = handle_command(user, UserRepository(session=DBSession.get_session()))
    return response


@router.patch("/update-user")
async def update_user(user: UpdateUser):
    response = handle_command(user, UserRepository(session=DBSession.get_session()))
    return response
