from fastapi import Response
from pydantic import BaseModel

class Payload(BaseModel):
    text: str


class ChatResponse(Response):
    def __init__(self, response:str, status:bool):
        self.response = response
        self.status = status
