from fastapi import APIRouter

# create user
router = APIRouter(prefix="/users", tags=["users"])


@router.post("/")
async def create_user_api():
    pass
