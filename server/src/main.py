from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from src.routes.post import router as Post

import src.database as database
import src.models as models

# Initialize database with downloaded data from external API
database.initialize_collection_posts()

# Add openAPI tags to Swagger
openapi_tags = [
    {
        "name": "Post",
        "description": "Endpoints are responsible for post operations.",
    },
]

# Create FastAPI app
app = FastAPI(
    title="Server",
    openapi_tags=openapi_tags,
)

# Add Middleware
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include router
app.include_router(Post)


@app.get("/", status_code=200, response_model=models.Content, tags=["Root"])
async def root():
    """
    The endpoint is responsible for returning simple hello message to check if server container is running.
    """
    content = {
        "status": "success",
        "message": "Hello World from the server container!",
    }
    return JSONResponse(status_code=status.HTTP_200_OK, content=content)
