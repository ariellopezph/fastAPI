from pydantic import BaseModel
from typing import Optional

class UserRquestModel(BaseModel):
    username: str
    email: Optional[str] = None


class UserResponseModel(UserRquestModel):
    id: int