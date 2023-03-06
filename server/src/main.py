# from threading import Thread
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# from fastapi.responses import HTMLResponse
# import requests
# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
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

@app.get("/", tags=["Root"])
async def root():
    """
    The function is responsible for returning simple hello message to check if server is running.
    """

    content = {
        "status": "success",
        "message": "Hello World!",
    }
    return JSONResponse(status_code=status.HTTP_200_OK, content=content)
