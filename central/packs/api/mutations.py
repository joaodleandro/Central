from strawberry import ID
from strawberry.types import Info
from core.strawberry import DeletePayload, ErrorType
from packs.api.inputs import (
    CreatePackageInput,
    CreateUserPackageInput,
    UpdatePackageInput,
    UpdateUserPackageInput,
)
from packs.api.payloads import PackagePayload, UserPackagePayload
from packs.forms import PackageForm, UserPackageForm
from packs.models import Package, UserPackage
from django.contrib.auth.decorators import permission_required


@permission_required("create-package")
def create_package_mutation(info: Info, input_: CreatePackageInput) -> PackagePayload:

    form = PackageForm(input_)

    if form.is_valid():
        form.save()

        return PackagePayload(
            success=True,
            errors=[],
            package=PackagePayload(form.instance),
        )

    return PackagePayload(
        success=False,
        errors=ErrorType.from_errors(form.errors),
        package=None,
    )


@permission_required("change-package")
def update_package_mutation(info: Info, input_: UpdatePackageInput) -> PackagePayload:

    try:
        package = Package.objects.get(
            id=input_.id,
        )
    except Package.DoesNotExist:
        return PackagePayload(
            success=False,
            errors=[ErrorType(field="id", messages=[("Package does not exist.")])],
            package=None,
        )

    form = PackageForm(input_, instance=package)

    if form.is_valid():
        form.save()

        return PackagePayload(
            success=True,
            errors=[],
            package=PackagePayload(form.instance),
        )

    return PackagePayload(
        success=False,
        errors=ErrorType.from_errors(form.errors),
        package=None,
    )


@permission_required("delete-package")
def delete_package_mutation(info: Info, id_: ID) -> DeletePayload:

    try:
        package = Package.objects.get(id=id_)
    except Package.DoesNotExist:
        return DeletePayload(
            success=True,
            errors=[],
        )

    package.delete()

    return DeletePayload(
        success=True,
        errors=[],
    )


@permission_required("create-user-package")
def create_user_package_mutation(
    info: Info, input_: CreateUserPackageInput
) -> UserPackagePayload:

    form = UserPackageForm(input_)

    if form.is_valid():
        form.save()

        return UserPackagePayload(
            success=True,
            errors=[],
            user_package=UserPackagePayload(form.instance),
        )

    return UserPackagePayload(
        success=False,
        errors=ErrorType.from_errors(form.errors),
        user_package=None,
    )


@permission_required("change-user-package")
def update_user_package_mutation(
    info: Info, input_: UpdateUserPackageInput
) -> UserPackagePayload:

    try:
        user_package = UserPackage.objects.get(
            id=input_.id,
        )
    except UserPackage.DoesNotExist:
        return UserPackagePayload(
            success=False,
            errors=[ErrorType(field="id", messages=[("User Package does not exist.")])],
            user_package=None,
        )

    form = UserPackageForm(input_, instance=user_package)

    if form.is_valid():
        form.save()

        return UserPackagePayload(
            success=True,
            errors=[],
            user_package=UserPackagePayload(form.instance),
        )

    return UserPackagePayload(
        success=False,
        errors=ErrorType.from_errors(form.errors),
        user_package=None,
    )


@permission_required("delete-user-package")
def delete_user_package_mutation(info: Info, id_: ID) -> DeletePayload:

    try:
        user_package = UserPackage.objects.get(id=id_)
    except UserPackage.DoesNotExist:
        return DeletePayload(
            success=True,
            errors=[],
        )

    user_package.delete()

    return DeletePayload(
        success=True,
        errors=[],
    )
