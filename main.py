from importlib import reload

import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get("/")
def index():
    return "Hello Fast!!"


if __name__ == "__main__":
    uvicorn.run("main:app")
