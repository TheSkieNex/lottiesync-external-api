import uvicorn
import logging
from fastapi import FastAPI

from server.router import router

def create_app():
    app = FastAPI()

    app.include_router(router)

    return app

if __name__ == '__main__':
    app = create_app()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    uvicorn.run(app, host='127.0.0.1', port=7262, log_level='info', access_log=False)