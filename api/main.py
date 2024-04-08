from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from chatbot_webapi import ChatBotAPI

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"])

chatapi = ChatBotAPI("api")
app.include_router(chatapi.router)
app.mount("/static", StaticFiles(directory="static"), name="static")
