import datetime
import strawberry
from strawberry import ID


@strawberry.type
class PackageType:
    id: ID
    name: str
    price: float
    created_at: datetime.datetime
    updated_at: datetime.datetime
    created_by: ID
    updated_by: ID


@strawberry.type
class UserPackageType:
    id: ID
    user: ID
    package: ID
    duration: datetime.datetime
    is_active: bool
