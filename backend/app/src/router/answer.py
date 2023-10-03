from fastapi import APIRouter


router: APIRouter = APIRouter()


@router.post(path=...)
def create_answer() -> ...:
    return
