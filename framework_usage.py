from urllib import response
from urllib.request import Request

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request: Request) -> JSONResponse:
    """home page

    Args:
        request (Request): _description_

    Returns:
        JSONResponse: _description_
    """
    return JSONResponse({'hello': 'world'})


app = Starlette(
    debug=True, routes=[
        Route('/', homepage)
    ]
)
