import datetime
import strawberry
from typing import Optional
from strawberry import ID, UNSET


@strawberry.input
class PackageFilter:
    id__in: Optional[list[Optional[ID]]] = UNSET
    name__icontains: Optional[str] = UNSET
    price: Optional[float] = UNSET
    created_at__lte: Optional[datetime.datetime] = UNSET
    created_at__gte: Optional[datetime.datetime] = UNSET
    updated_at__lte: Optional[datetime.datetime] = UNSET
    updated_at__gte: Optional[datetime.datetime] = UNSET
    created_by__in: Optional[ID] = UNSET
    updated_by__in: Optional[ID] = UNSET


@strawberry.input
class UserPackageFilter:
    id__in: Optional[list[Optional[ID]]] = UNSET
    user: Optional[ID] = UNSET
    package: Optional[ID] = UNSET
    is_active: Optional[bool] = UNSET
