from typing import Annotated

from fastapi import Depends, Request
from vital import AsyncVital as _AsyncVital


def get_async_vital_client_dep(request: Request) -> _AsyncVital:
    return request.app.state.async_vital


AsyncVital = Annotated[_AsyncVital, Depends(get_async_vital_client_dep)]
