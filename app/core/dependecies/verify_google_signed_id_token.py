from typing import NewType

from fastapi import Depends, Header, HTTPException, status
from google.auth.transport.requests import Request as GoogleAuthRequest
from google.oauth2 import id_token

from app.core.settings import settings

__all__ = ("verify_google_signed_id_token",)


GoogleSignedIdToken = NewType("GoogleSignedIdToken", str)


def _raise_invalid_token_http_exception() -> None:
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid google signed id token token",
    )


def _get_google_signed_id_token_from_header(
    authorization_header_value: str = Header(alias="Authorization"),
) -> GoogleSignedIdToken:
    if not authorization_header_value.startswith("Bearer"):
        _raise_invalid_token_http_exception()

    try:
        return authorization_header_value.split(" ")[-1]
    except KeyError:
        _raise_invalid_token_http_exception()


def verify_google_signed_id_token(
    google_signed_id_token: GoogleSignedIdToken = Depends(_get_google_signed_id_token_from_header),
) -> None:
    try:
        id_token.verify_oauth2_token(
            google_signed_id_token,
            GoogleAuthRequest(),
            audience=settings.AUDIENCE,
        )
    except ValueError:
        _raise_invalid_token_http_exception()
