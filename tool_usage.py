from starlette.responses import PlainTextResponse


async def app(scope, receive, send):
    """_summary_

    Args:
        scope (_type_): _description_
        receive (_type_): _description_
        send (_type_): _description_
    """
    assert scope['type'] == 'http'
    response = PlainTextResponse('Hello World')
    await response(scope, receive, send)
