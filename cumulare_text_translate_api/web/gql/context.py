from fastapi import Depends
from strawberry.fastapi import BaseContext


class Context(BaseContext):
    """Global graphql context."""

    def __init__(
        self,
    ) -> None:
        pass  # noqa: WPS420


def get_context(context: Context = Depends(Context)) -> Context:
    """
    Get custom context.

    :param context: graphql context.
    :return: context
    """
    return context
