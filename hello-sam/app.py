from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(root_path="/Prod")


@app.get("/")
def root():
    return {"message": "hello"}


handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
