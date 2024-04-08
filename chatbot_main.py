import argparse
from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware

from chatbot_webapi import ChatBotAPI

api_app = FastAPI()
api_app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"])

chatapi = ChatBotAPI("api")
api_app.include_router(chatapi.router)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Chatbot API",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-t", "--host", default="localhost", help="the host to expose the API"
    )

    parser.add_argument(
        "-p", "--port", type=int, default=8000, help="The port to expose the API"
    )

    args = parser.parse_args()

    uvicorn.run(api_app, host=args.host, port=args.port)
