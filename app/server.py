from fastapi import FastAPI
from langserve import add_routes

from app.agent_executor import agent_executor as agent_chain

app = FastAPI()


add_routes(app, agent_chain, path="/agent_chain")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
