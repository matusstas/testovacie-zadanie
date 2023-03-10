import requests
from fastapi import Request
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Create FastAPI router
router = APIRouter(
    tags=["Post"],
)

# Add templates directory
templates = Jinja2Templates(directory="src/static/templates")


@router.get("/posts", response_class=HTMLResponse)
async def get_page_posts(request: Request):
    """
    The endpoint is responsible for returning page with all its posts.
    """
    posts = requests.get("http://server:80/posts").json()["posts"]
    return templates.TemplateResponse("html/posts.html", {"request": request, "posts": posts})


@router.get("/posts/{id}", response_class=HTMLResponse)
async def get_page_post(request: Request, id: int):
    """
    The endpoint is responsible for returning post detail page by its id.
    """
    post = requests.get(f"http://server:80/posts/{id}").json()
    return templates.TemplateResponse("html/post.html", {"request": request, "post": post})


@router.get("/create", response_class=HTMLResponse)
async def get_create_page_post(request: Request):
    """
    The endpoint is responsible for returning create post page.
    """
    return templates.TemplateResponse("html/create.html", {"request": request})


@router.delete("/posts/{id}")
async def delete_post(id: int):
    """
    The endpoint is responsible for deleting post by its id.
    """
    requests.delete(f"http://server:80/posts/{id}")


@router.put("/posts/{id}")
async def update_post(request: Request, id: int):
    """
    The endpoint is responsible for updating post by its id.
    """
    post = await request.json()
    headers = {"Content-Type": "application/json", "accept": "application/json"}
    result = requests.put(f"http://server:80/posts/{id}", headers=headers, json=post)
    return result


@router.post("/post")
async def create_post(request: Request):
    """
    The endpoint is responsible for creating new post.
    """
    post = await request.json()
    headers = {"Content-Type": "application/json", "accept": "application/json"}
    result = requests.post(f"http://server:80/post", headers=headers, json=post).json()
    return result
