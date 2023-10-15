import strawberry
from strawberry.fastapi import GraphQLRouter

from cumulare_text_translate_api.web.gql import echo
from cumulare_text_translate_api.web.gql.context import Context, get_context


@strawberry.type
class Query(  # noqa: WPS215
    echo.Query,
):
    """Main query."""


@strawberry.type
class Mutation(  # noqa: WPS215
    echo.Mutation,
):
    """Main mutation."""


schema = strawberry.Schema(
    Query,
    Mutation,
)

gql_router: GraphQLRouter[Context, None] = GraphQLRouter(
    schema,
    graphiql=True,
    context_getter=get_context,
)
