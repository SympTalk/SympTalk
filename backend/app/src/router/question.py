from fastapi import APIRouter


router: APIRouter = APIRouter()


@router.get(path=...)
def get_question() -> ...:
    return
