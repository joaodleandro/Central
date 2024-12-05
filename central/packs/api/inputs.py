import datetime
import strawberry
from strawberry import ID, UNSET


@strawberry.input
class CreatePackageInput:
    name: str
    price: float


@strawberry.input
class UpdatePackageInput(CreatePackageInput):
    id: ID


@strawberry.input
class CreateUserPackageInput:
    user: ID
    package: ID
    duration: datetime.datetime
    is_active: bool


@strawberry.input
class UpdateUserPackageInput(CreateUserPackageInput):
    id: ID
