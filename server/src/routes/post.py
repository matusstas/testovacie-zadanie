import requests
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

import src.database as database
import src.models as models

# Create FastAPI router
router = APIRouter(
    tags=["Post"],
)


@router.post("/post",
            status_code=200,
            response_model=models.Post,
            responses = {
                404: {
                    "model": models.Content,
                    "content": {
                        "application/json": {
                            "examples": {
                                "-": {
                                    "value": {
                                        "status": "error",
                                        "message": "User does not exist",
                                    },
                                },
                            },
                        },
                    },
                },
            })
async def create_post(post: models.Post2):
    """
    The endpoint is responsible for creating post. Validation of UserId with external API mandatory.
    """
    userId = post.userId
    title = post.title
    body = post.body

    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{userId}").json()
    if bool(user) is False:
        content = {
            "status": "error",
            "message": "User does not exist",
        }
        return JSONResponse(status_code=404, content=content)
    else:
        database.create_post(userId, title, body)
        id_max = database.get_id_max()
        post = database.get_post(id_max)
        return post


@router.get("/posts/{id}",
            status_code=200,
            response_model=models.Post,
            responses = {
                404: {
                    "model": models.Content,
                    "content": {
                        "application/json": {
                            "examples": {
                                "-": {
                                    "value": {
                                        "status": "error",
                                        "message": "Post does not exist",
                                    },
                                },
                            },
                        },
                    },
                },
            })
async def get_post(id: int):
    """
    The endpoint is responsible for returning post by its id.
    """
    post = database.get_post(id)
    if post is None:
        content = {
            "status": "error",
            "message": "Post does not exist",
        }
        return JSONResponse(status_code=404, content=content)
    else:
        return post


@router.put("/posts/{id}",
            status_code=200,
            response_model=models.Post,
            responses = {
                404: {
                    "model": models.Content,
                    "content": {
                        "application/json": {
                            "examples": {
                                "-": {
                                    "value": {
                                        "status": "error",
                                        "message": "Post does not exist",
                                    },
                                },
                            },
                        },
                    },
                },
            })
async def update_post(id: int, post: models.Post):
    """
    The endpoint is responsible for updating post's title and body by its id.
    """    
    id = post.id
    title = post.title
    body = post.body

    post = database.get_post(id)
    if post is None:
        content = {
            "status": "error",
            "message": "Post does not exist",
        }
        return JSONResponse(status_code=404, content=content)
    else:
        database.update_post(id, title, body)
        post = database.get_post(id)
        return post


@router.delete("/posts/{id}",
            status_code=200,
            responses = {
                404: {
                    "model": models.Content,
                    "content": {
                        "application/json": {
                            "examples": {
                                "-": {
                                    "value": {
                                        "status": "error",
                                        "message": "Post does not exist",
                                    },
                                },
                            },
                        },
                    },
                },
            })
async def delete_post(id: int):
    """
    The endpoint is responsible for deleting post by its id.
    """
    post = database.get_post(id)
    if post is None:
        content = {
            "status": "error",
            "message": "Post does not exist",
        }
        return JSONResponse(status_code=404, content=content)
    else:
        database.delete_post(id)


@router.get("/posts", status_code=200, response_model=models.Posts)
async def get_posts():
    """
    The endpoint is responsible for returning  all posts.
    """
    posts = database.get_posts()
    return posts
