import logging
import uvicorn

from fastapi import FastAPI

from server.router import router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("server.log", mode='a'), logging.StreamHandler()]
)

def create_app():
    app = FastAPI()

    app.include_router(router)

    return app

if __name__ == '__main__':
    app = create_app()

    uvicorn.run(app, host='127.0.0.1', port=7262, log_config=None)