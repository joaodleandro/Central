import datetime
import strawberry
from strawberry import ID


@strawberry.type
class UserType:
    id: ID
    password: str
    last_login: datetime.datetime
    is_superuser: bool
    username: str
    first_name: str
    last_name: str
    email: str
    is_staff: bool
    is_active: bool
    date_joined: datetime.datetime
