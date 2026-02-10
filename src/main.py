from fastapi import FastAPI

app = FastAPI()


@app.post("/shorten")
async def shorten():
    ...

@app.get("/{code}")
async def redirect():
    ...
