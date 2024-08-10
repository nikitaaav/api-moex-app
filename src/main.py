from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.parser import get_info


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/api/stock/{tkr}")
def stock_info(tkr: str):
    if tkr is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Акция не найдена"}
        )
    info = get_info(tkr)
    return info


# uvicorn src.main:app --reload
# https://bcs.ru/markets