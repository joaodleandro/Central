from typing import Optional
from strawberry import ID
from strawberry.types import Info

from .filters import UserFilter
from ..models import User
from .types import UserType
from django.contrib.auth.decorators import permission_required


@permission_required("view_user")
def get_user_resolver(info: Info, id_: ID) -> Optional[UserType]:
    return UserType(**User.objects.get(id=id_))


@permission_required("view_user")
def list_user_resolver(info: Info, filter_: Optional[UserFilter]) -> list[UserType]:
    queryset = User.objects.all().filter(**filter_)
    return [UserType(item) for item in queryset]
