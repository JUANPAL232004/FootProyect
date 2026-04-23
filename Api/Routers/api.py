from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="Frontend/Static"), name="static")
templates = Jinja2Templates(directory="./Frontend/templates")

@app.get("/Home", response_class=HTMLResponse)
async def get_login(request: Request):
    return templates.TemplateResponse(
        request=request, name="Home.html", context={"request": request}
    )

@app.get("/Menu", response_class=HTMLResponse)
async def get_register(request: Request):
    return templates.TemplateResponse(
        request=request, name="menu.html", context={"request": request}
    )