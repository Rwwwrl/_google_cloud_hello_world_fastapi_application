import logging

from fastapi import APIRouter, Request, Response, status
from fastapi.templating import Jinja2Templates

from fastapi_hello_world.core.settings import BASE_DIR, settings
from fastapi_hello_world.users import repositories, schemas

users_api_router = APIRouter(tags=["users"])

templates = Jinja2Templates(directory=BASE_DIR / "users" / "templates")


logger = logging.getLogger(__name__)


@users_api_router.get("")
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
    "",
    responses={
        status.HTTP_201_CREATED: {"model": Response},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": Response},
    },
)
async def create_user(payload: schemas.CreateUserPayload) -> Response:
    try:
        await repositories.UserRepository.create_new_user(
            new_user_payload=repositories.CreateNewUserDTO(
                google_identity=repositories.GoogleIdentityPlatformDataDTO(
                    uid=payload.uid,
                    tenant_id=payload.tenant_id,
                    email=payload.email,
                ),
            )
        )
    except repositories.ExceptionDuringWriting:
        logger.exception()
        return Response(
            content="exception during saving new user",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return Response(status_code=status.HTTP_201_CREATED)
