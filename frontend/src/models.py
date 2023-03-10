from pydantic import BaseModel

class Content(BaseModel):
    status: str
    message: str
