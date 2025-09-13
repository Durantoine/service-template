from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


def hello(name: str) -> str:
    return f"Hello {name}"


@app.get("/", response_class=PlainTextResponse)
async def root() -> str:
    return "Hello world"
