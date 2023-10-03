from fastapi import FastAPI

from src.router import router


app: FastAPI = FastAPI()
app.include_router(router=router)


if __name__ == "__main__":
    import uvicorn


    uvicorn.run(app="src.main:app", reload=True)
