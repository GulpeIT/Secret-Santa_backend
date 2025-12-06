from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    surname: str

class UserRead(UserBase):
    id: int