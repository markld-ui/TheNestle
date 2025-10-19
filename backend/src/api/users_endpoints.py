from fastapi import APIRouter, HTTPException, Depends

from schemas.user_shemas import UserShemaAdd, UserShema, UserShemaId
from repositories.user_repository import UserRepository

router = APIRouter(prefix="/users", tags=["users"])

# users : UserShema = [
#     UserShema(
#         name = "123",
#         bio = "123",
#         email = "thankr3@gmail.com",
#         age = 12,
#     )
# ]

users : UserShemaAdd = []


@router.get("/", summary="Get all users")
async def get_users() -> list[UserShema]:
    user = await UserRepository.get_users()
    return user


@router.post("/", summary="Create a new user")
async def create_user(new_user: UserShemaAdd = Depends()) -> UserShemaId:
    user_id = await UserRepository.add_user(new_user)
    return UserShemaId(id=user_id)


@router.get("/{user_id}", summary="Get a user")
async def get_user(user_id: int) -> UserShema:
    user = await UserRepository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user