from sqlalchemy import select

from models.user_model import UserOrm
from database import new_session
from schemas.user_shemas import UserShemaAdd, UserShema


class UserRepository:
    @classmethod
    async def add_user(cls, user: dict) -> int:
       async with new_session() as session:
           data = user.model_dump()
           new_user = UserOrm(**data)
           session.add(new_user)
           await session.flush()
           await session.commit()
           return new_user.id


    @classmethod
    async def get_users(cls) -> list[UserShema]:
       async with new_session() as session:
           query = select(UserOrm)
           result = await session.execute(query)
           user_models = result.scalars().all()
           users = [UserShema.model_validate(user_model) for user_model in user_models]
           return users


    @classmethod
    async def get_user_by_id(cls, user_id: int) -> UserShema:
        async with new_session() as session:
            query = select(UserOrm).where(UserOrm.id == user_id)
            result = await session.execute(query)
            user_model = result.scalar_one_or_none()
            if user_model:
                return UserShema.model_validate(user_model)
            return None