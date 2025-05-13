import logging

from fastapi import APIRouter, Depends, Request, Response, status
from fastapi.templating import Jinja2Templates

from app.api.users.repositories import UserRepository
from app.api.users.schemas import dtos, request_schemas
from app.core.dependecies.verify_google_signed_id_token import _get_google_signed_id_token_from_header
from app.core.settings import BASE_DIR, settings

users_api_router = APIRouter(tags=["users"])

templates = Jinja2Templates(directory=BASE_DIR / "api" / "users" / "templates")


logger = logging.getLogger(__name__)


@users_api_router.post("/ping/")
async def hello_world(token: str = Depends(_get_google_signed_id_token_from_header)):
    print(token)
    return Response(status_code=200)


@users_api_router.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "api_key": settings.FIREBASE_CONFIG.api_key,
            "auth_domain": settings.FIREBASE_CONFIG.auth_domain,
        },
    )


@users_api_router.post(
    "/",
    responses={
        status.HTTP_201_CREATED: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
    },
    include_in_schema=False,
)
async def create_user_gcloud_fallback(payload: request_schemas.CreateUserPayload) -> Response:
    try:
        await UserRepository.create_new_user(
            new_user_payload=dtos.CreateNewUserDTO(
                google_identity=dtos.GCloudIdentityPlatformDataDTO(
                    uid=payload.uid,
                    email=payload.email,
                ),
            )
        )
    except Exception:
        logger.exception()
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(status_code=status.HTTP_201_CREATED)
