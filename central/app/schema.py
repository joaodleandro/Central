import strawberry
from strawberry.tools import merge_types
from users.api.schema import (
    Query as UserQuery,
    Mutation as UserMutation,
    Query as PackageQuery,
    Mutation as PackageMutation,
)

Query = merge_types(
    "Query",
    (
        UserQuery,
        PackageQuery,
    ),
)
Mutation = merge_types(
    "Mutation",
    (
        UserMutation,
        PackageMutation,
    ),
)

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
