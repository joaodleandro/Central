import strawberry
from typing import Optional
from core.strawberry import BasePayload
from users.api.types import UserType


@strawberry.type
class UserPayload(BasePayload):
    user: Optional[UserType]
