from fastapi import FastAPI, APIRouter


router = APIRouter(prefix='/api')


@router.get("")
async def ping():
    return 'pong'


def add_routes(app: FastAPI):
    app.include_router(router)
