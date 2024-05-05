import datetime
import strawberry
from typing import Optional
from strawberry import ID, UNSET


@strawberry.input
class CreateUserInput:
    password: str
    last_login: Optional[datetime.datetime] = UNSET
    is_superuser: Optional[bool] = UNSET
    username: str
    first_name: Optional[str] = UNSET
    last_name: Optional[str] = UNSET
    email: Optional[str] = UNSET
    is_staff: Optional[bool] = UNSET
    is_active: Optional[bool] = UNSET
    date_joined: Optional[datetime.datetime] = UNSET


@strawberry.input
class UpdateUserInput(CreateUserInput):
    id: ID
