# from threading import Thread
from fastapi import FastAPI, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# from fastapi.responses import HTMLResponse
# import requests
# from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import RedirectResponse
# import json
# import random
# from fastapi.responses import FileResponse
# from datetime import datetime


# import src.database as database
# import src.helper as h

# Create FastAPI app
app = FastAPI()

# Add Middleware
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount templates and static files
templates = Jinja2Templates(directory="src/static/templates")
app.mount("/static", StaticFiles(directory="src/static"), name="static")


@app.get("/", tags=["Root"])
async def root():
    """
    The function is responsible for returning simple hello message to check if server is running.
    """

    content = {
        "status": "success",
        "message": "Hello World from ui container!",
    }
    return JSONResponse(status_code=status.HTTP_200_OK, content=content)

# todo
@app.get("/posts", response_class=HTMLResponse)
async def home(request: Request):
    """
    todo
    """
    return templates.TemplateResponse("posts.html", {"request": request})

# todo
@app.get("/post", response_class=HTMLResponse)
async def home(request: Request):
    """
    todo
    """
    return templates.TemplateResponse("post-old.html", {"request": request})


# todo
@app.get("/base", response_class=HTMLResponse)
async def home(request: Request):
    """
    todo
    """
    return templates.TemplateResponse("child.html", {"request": request})
