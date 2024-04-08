import json
from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from re_edge_gpt import Chatbot, ConversationStyle

from chatbot_payload import Payload

class ChatBotAPI:
    def __init__(self, name:str):
        self.name = name
        self.router = APIRouter()
        self.router.add_api_route(f"/{name}/post-response", self.post_response, methods=["POST"])
        self.router.add_api_route(f"/{name}/ask-question", self.get_response, methods=["GET"])

    async def send_request(self, question):
        cookies = json.loads(open(str(Path(str(Path.cwd()) + "./bing-cookies.txt")), encoding="utf-8").read())
        bot = await Chatbot.create(cookies=cookies)

        response = await bot.ask(prompt=question, conversation_style=ConversationStyle.creative,
                                simplify_response=True)
        answer = response['text']
        res = {"response": answer}
        return JSONResponse(res, 200)
    
    async def post_response(self, payload: Payload):
        message = await self.send_request(payload.text)
        return  message
    
    async def get_response(self, question):
        message = await self.send_request(question)
        return  message
    
