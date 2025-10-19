import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.users_endpoints import router as users_router

from contextlib import asynccontextmanager
from database import create_tables, delete_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
   await create_tables()
   print("База готова")
   yield
   await delete_tables()
   print("База очищена")

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)


app.include_router(users_router)


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
