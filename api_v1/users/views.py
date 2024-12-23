from fastapi import APIRouter, status, Depends
from api_v1.users.schemas import User, UserEdit
from .dependencies import get_user_by_id

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "/one",
    response_model=User,
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_404_NOT_FOUND: {"description": "User not found"}},
    description="Endpoint to get a user",
)
async def get_user(
    user: User = Depends(get_user_by_id),
):
    return user
