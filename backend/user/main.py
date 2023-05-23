import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter

from .api.routes.account import user_router
from .api.routes.authentication import login_router
from config.manager import settings


# create instance of the app
app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
    docs_url=settings.DOCS_URL,
    debug=settings.DEBUG,
)

# create the instance for the routes
main_api_router = APIRouter()

# set routes to the app instance
main_api_router.include_router(user_router, prefix="/user", tags=["user"])
main_api_router.include_router(login_router, prefix="/login", tags=["login"])
app.include_router(main_api_router)

if __name__ == "__main__":
    # run app on the host and port
    uvicorn.run(app, host="0.0.0.0", port=8000)
