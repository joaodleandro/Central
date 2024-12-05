import datetime
import strawberry
from typing import Optional
from strawberry import ID, UNSET


@strawberry.input
class UserFilter:
    id__in: Optional[list[Optional[ID]]] = UNSET
    password__icontains: Optional[str] = UNSET
    last_login__lte: Optional[datetime.datetime] = UNSET
    last_login__gte: Optional[datetime.datetime] = UNSET
    is_superuser: Optional[bool] = UNSET
    username__icontains: Optional[str] = UNSET
    first_name__icontains: Optional[str] = UNSET
    last_name__icontains: Optional[str] = UNSET
    email__icontains: Optional[str] = UNSET
    is_staff: Optional[bool] = UNSET
    is_active: Optional[bool] = UNSET
