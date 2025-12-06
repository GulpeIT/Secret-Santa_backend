from pydantic import BaseModel


class UserBase(BaseModel):
    phone_number: str
    username: str
    name: str
    surname: str

class UserRead(UserBase):
    id: int

class UserCreate(UserBase):
    ...