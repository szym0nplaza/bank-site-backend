from fastapi import APIRouter, Request, Response
from modules.accounts.application.commands import CreateUser


accounts_router = router = APIRouter()


@router.post("/create-user")
async def create_user(user: CreateUser):
    print(user)
    return Response({"message":"ok"}, status_code=200)
