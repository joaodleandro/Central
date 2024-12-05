from typing import Optional

import strawberry


@strawberry.type
class ErrorType:
    messages: list[str]
    field: str

    @classmethod
    def from_errors(cls, errors) -> list["ErrorType"]:
        if isinstance(errors, list):
            return [
                cls(field=error["field"], messages=error["messages"])
                for error in errors
            ]
        return [
            cls(field=key, messages=value.data[0].messages)
            for key, value in errors.items()
        ]


@strawberry.interface
class BasePayload:
    success: bool
    errors: Optional[list[ErrorType]]


@strawberry.type
class DeletePayload(BasePayload):
    pass
