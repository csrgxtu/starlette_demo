from urllib.request import Request

from starlette.applications import Starlette
from starlette.responses import JSONResponse, PlainTextResponse
from starlette.routing import Route, WebSocketRoute


async def homepage(request: Request) -> JSONResponse:
    """home page

    Args:
        request (Request): _description_

    Returns:
        JSONResponse: _description_
    """
    return JSONResponse({'hello': 'world'})


async def user_me(request: Request) -> PlainTextResponse:
    """_summary_

    Args:
        request (Request): _description_

    Returns:
        PlainTextResponse: _description_
    """
    return PlainTextResponse(f'Hello Archer')


async def user(request: Request) -> PlainTextResponse:
    """_summary_

    Args:
        request (Request): _description_

    Returns:
        PlainTextResponse: _description_
    """
    return PlainTextResponse(f'Hello {request.path_params["username"]}')


async def websocket_endpoint(websocket):
    """_summary_

    Args:
        websocket (_type_): _description_
    """
    await websocket.accept()
    await websocket.send_text('Hello websocket')
    await websocket.close()


async def startup() -> None:
    """_summary_
    """
    print('Read to go')


routes = [
    Route('/', homepage),
    Route('/user/me', user_me),
    Route('/user/{username}', user),
    WebSocketRoute('/ws', websocket_endpoint),
]
app = Starlette(
    debug=True, routes=routes, on_startup=[startup]
)
