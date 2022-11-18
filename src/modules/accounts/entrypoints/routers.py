from fastapi import APIRouter
from fastapi.responses import JSONResponse
from modules.accounts.application.commands import CreateUser
from base.handlers import handle_command
from modules.accounts.infrastructure.repositories import UserRepository
from config.settings import DBSession


accounts_router = router = APIRouter()


@router.post("/create-user")
async def create_user(user: CreateUser):
    handle_command(user, UserRepository(session=DBSession.get_session()))
    return JSONResponse({"message":"ok"}, status_code=200)
