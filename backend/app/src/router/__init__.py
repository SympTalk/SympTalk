from fastapi import APIRouter

from src.router import answer, question


router: APIRouter = APIRouter()
router.include_router(router=answer.router)
router.include_router(router=question.router)
