import strawberry
from typing import Optional
from packs.api.mutations import (
    create_package_mutation,
    create_user_package_mutation,
    delete_package_mutation,
    delete_user_package_mutation,
    update_package_mutation,
    update_user_package_mutation,
)
from packs.api.queries import (
    get_package_resolver,
    get_user_package_resolver,
    list_package_resolver,
    list_user_package_resolver,
)
from packs.api.types import PackageType, UserPackageType
from packs.api import payloads


@strawberry.type
class Query:
    # Package
    get_package: Optional[PackageType] = strawberry.field(resolver=get_package_resolver)
    list_packages: list[PackageType] = strawberry.field(resolver=list_package_resolver)

    # User Packages
    get_user_package: Optional[UserPackageType] = strawberry.field(
        resolver=get_user_package_resolver
    )
    list_user_packages: list[UserPackageType] = strawberry.field(
        resolver=list_user_package_resolver
    )


@strawberry.type
class Mutation:
    # Package
    create_package: payloads.PackagePayload = strawberry.field(
        resolver=create_package_mutation
    )
    update_package: payloads.PackagePayload = strawberry.field(
        resolver=update_package_mutation
    )
    delete_package: payloads.PackagePayload = strawberry.field(
        resolver=delete_package_mutation
    )

    # User Packages
    create_user_package: payloads.UserPackagePayload = strawberry.field(
        resolver=create_user_package_mutation
    )
    update_user_package: payloads.UserPackagePayload = strawberry.field(
        resolver=update_user_package_mutation
    )
    delete_user_package: payloads.UserPackagePayload = strawberry.field(
        resolver=delete_user_package_mutation
    )
