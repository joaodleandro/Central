import strawberry
from typing import Optional
from core.strawberry import BasePayload
from users.api.types import PackageType, UserPackageType


@strawberry.type
class PackagePayload(BasePayload):
    package: Optional[PackageType]


@strawberry.type
class UserPackagePayload(BasePayload):
    user_package: Optional[UserPackageType]
