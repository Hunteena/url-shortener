from contextlib import asynccontextmanager
import os
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import RedirectResponse

from src import db
from src.logger import logger
from src.models import ShortenRequest, ShortenResponse
from src.utils import generate_random_code


BASE_URL = os.getenv("BASE_URL", "http://localhost:8000").rstrip("/")


@asynccontextmanager
async def startup(app: FastAPI):
    db.init_db()
    yield

app = FastAPI(lifespan=startup)

@app.post(
    "/shorten",
    response_model=ShortenResponse,
    status_code=status.HTTP_201_CREATED,
)
async def shorten(cmd: ShortenRequest):
    try: 
        duplicate = "not empty"
        while duplicate:
            code = generate_random_code()
            duplicate = db.get_by_code(code)
        db.create_row(str(cmd.url), code)
        short = f"{BASE_URL}/{code}"
        logger.info("Created short url %s for url %s", short, cmd.url)
        return {"short_url": short, "code": code, "url": cmd.url}
    except Exception as e:
        logger.exception("Error creating short url")
        raise HTTPException(status_code=500, detail="internal error")


@app.get(
    "/{code}",
    response_class=RedirectResponse,
)
async def redirect(code: str):    
    row = db.get_by_code(code)
    if not row:
        logger.info("Redirect attempted for unknown code: %s", code)
        raise HTTPException(status_code=404, detail="Not found")
    logger.info("Redirecting code=%s to url=%s", code, row["url"])
    return row["url"]
