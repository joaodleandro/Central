from strawberry import ID
from strawberry.types import Info
from core.strawberry import DeletePayload, ErrorType
from users.api.inputs import CreateUserInput, UpdateUserInput
from users.api.payloads import UserPayload
from users.forms import UserForm
from ..models import User
from django.contrib.auth.decorators import permission_required


@permission_required("create-user")
def create_user_mutation(info: Info, input_: CreateUserInput) -> UserPayload:

    form = UserForm(input_)

    if form.is_valid():
        form.save()

        return UserPayload(
            success=True,
            errors=[],
            user=UserPayload(form.instance),
        )

    return UserPayload(
        success=False,
        errors=ErrorType.from_errors(form.errors),
        user=None,
    )


@permission_required("change-user")
def update_user_mutation(info: Info, input_: UpdateUserInput) -> UserPayload:

    try:
        user = User.objects.get(
            id=input_.id,
        )
    except User.DoesNotExist:
        return UserPayload(
            success=False,
            errors=[ErrorType(field="id", messages=[("User does not exist.")])],
            user=None,
        )

    form = UserForm(input_, instance=user)

    if form.is_valid():
        form.save()

        return UserPayload(
            success=True,
            errors=[],
            user=UserPayload(form.instance),
        )

    return UserPayload(
        success=False,
        errors=ErrorType.from_errors(form.errors),
        user=None,
    )


@permission_required("delete-user")
def delete_user_mutation(info: Info, id_: ID) -> DeletePayload:

    try:
        user = User.objects.get(id=id_)
    except User.DoesNotExist:
        return DeletePayload(
            success=True,
            errors=[],
        )

    user.delete()

    return DeletePayload(
        success=True,
        errors=[],
    )
