from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    print("hello")
    return {"hello": "world"}


@app.get("/health")
def healthy():
    return {"health": 200}
