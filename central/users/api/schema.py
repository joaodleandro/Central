import strawberry
from typing import Optional


from users.api import payloads
from users.api.mutations import (
    create_user_mutation,
    delete_user_mutation,
    update_user_mutation,
)
from users.api.queries import get_user_resolver, list_user_resolver
from users.api.types import UserType


@strawberry.type
class Query:
    get_user: Optional[UserType] = strawberry.field(resolver=get_user_resolver)
    list_users: list[UserType] = strawberry.field(resolver=list_user_resolver)


@strawberry.type
class Mutation:
    create_user: payloads.UserPayload = strawberry.field(resolver=create_user_mutation)
    update_user: payloads.UserPayload = strawberry.field(resolver=update_user_mutation)
    delete_user: payloads.UserPayload = strawberry.field(resolver=delete_user_mutation)
