import datetime
import strawberry
from typing import Optional
from strawberry import ID


@strawberry.input
class CreateUserInput:
    password: str
    last_login: Optional[datetime.datetime]
    is_superuser: Optional[bool]
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    is_staff: Optional[bool]
    is_active: Optional[bool]
    date_joined: Optional[datetime.datetime]


@strawberry.input
class UpdateUserInput(CreateUserInput):
    id: ID
