from typing import Optional
from strawberry import ID
from strawberry.types import Info
from .filters import PackageFilter, UserPackageFilter
from ..models import Package, UserPackage
from .types import PackageType, UserPackageType
from django.contrib.auth.decorators import permission_required


@permission_required("view_package")
def get_package_resolver(info: Info, id_: ID) -> Optional[PackageType]:
    return PackageType(**Package.objects.get(id=id_))


@permission_required("view_package")
def list_package_resolver(
    info: Info, filter_: Optional[PackageFilter]
) -> list[PackageType]:
    queryset = Package.objects.all().filter(**filter_)
    return [PackageType(item) for item in queryset]


@permission_required("view_user_package")
def get_user_package_resolver(info: Info, id_: ID) -> Optional[UserPackageType]:
    return UserPackageType(**UserPackage.objects.get(id=id_))


@permission_required("view_user_package")
def list_user_package_resolver(
    info: Info, filter_: Optional[UserPackageFilter]
) -> list[UserPackageType]:
    queryset = UserPackage.objects.all().filter(**filter_)
    return [UserPackageType(item) for item in queryset]
