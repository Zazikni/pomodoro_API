from fastapi import APIRouter, status, Depends
from api_v1.users.schemas import User, UserEdit
from .dependencies import get_user_by_id, create_user_by_request

router = APIRouter(prefix="/users", tags=["Users"])


@router.get(
    "/",
    response_model=User,
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_404_NOT_FOUND: {"description": "User not found"}},
    description="Endpoint to get a user",
)
async def get_user(
    user: User = Depends(get_user_by_id),
):
    return user


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    # responses={status.HTTP_404_NOT_FOUND: {"description": "User not found"}},
    description="Endpoint to create user",
)
async def create_user(user: User = Depends(create_user_by_request)):
    return user
