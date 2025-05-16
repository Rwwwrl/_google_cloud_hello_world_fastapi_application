from fastapi import APIRouter, Depends, Response, status

from app.core.dependecies.verify_google_signed_id_token import verify_google_signed_id_token

hello_world_api_router = APIRouter(tags=["hello-world"])


@hello_world_api_router.post(
    "/test_protected_with_google_JWT_token_endpoint/",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(verify_google_signed_id_token)],
)
def protected_with_google_JWT_token_endpoint() -> Response:
    return Response(status_code=status.HTTP_200_OK)
