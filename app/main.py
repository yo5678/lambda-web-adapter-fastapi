from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    print("in root method")
    return {"message": "Hello World"}


# # TODO response_class=HTMLResponseと指定しているのが謎
# # TODO contestやrequestを指定しないと動作しないのがなぜかわかっていない

@app.get("/page", response_class=HTMLResponse)
async def read_page(request: Request):
    context = {"request": request, "message": "Hello, FastAPI with Jinja2!"}
    return templates.TemplateResponse("index.html", context)
