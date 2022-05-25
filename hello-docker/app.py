from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "hello"}

@app.get("/hello2")
def hello2():
    return {"message": "hello"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
