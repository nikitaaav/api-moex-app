from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.parser import get_info
import asyncio

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/api/stock/{tkr}")
async def stock_info(tkr: str):
    if tkr is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Акция не найдена"}
        )
    info_task = asyncio.create_task(get_info(tkr))
    info = await info_task

    return info


# uvicorn src.main:app --reload
# https://bcs.ru/markets