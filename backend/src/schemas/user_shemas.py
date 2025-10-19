from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserShemaAdd(BaseModel):
    name: str = Field(max_length=100)
    bio: str | None = Field(max_length=300)
    email: EmailStr
    age: int = Field(ge=0, le=100)


class UserShema(UserShemaAdd):
   id: int
   model_config = ConfigDict(from_attributes=True)


class UserShemaId(BaseModel):
   id: int