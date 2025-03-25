import uvicorn
from fastapi import FastAPI

from api.routers import router
from src.models import reset_tables

app = FastAPI()

app.include_router(router=router)


if __name__ == '__main__':
    reset_tables()
    uvicorn.run('main:app', reload=True)
