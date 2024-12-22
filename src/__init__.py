from fastapi import FastAPI
from src.books.routes import book_router
from src.auth.routes import auth_router
from src.reviews.routes import review_router
from contextlib import asynccontextmanager
from src.db.main import init_db


@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"server is starting....")
    await init_db()
    yield
    print(f"server is stopping....")



version = "v1"

app = FastAPI(
    title="Book API",
    description ="A REST API for a book review web service",
    version=version,
    

    )

app.include_router(book_router,prefix = f"/api/{version}/books",tags=['books'])
app.include_router(auth_router,prefix = f"/api/{version}/auth",tags=['auth'])
app.include_router(review_router,prefix = f"/api/{version}/reviews",tags=['reviews'])
