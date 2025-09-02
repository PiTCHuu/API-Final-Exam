from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
async def root():
    return {"message": "pong"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
