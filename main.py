from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World, this is server 2"}


@app.get("/be2", status_code=200)
async def be2():
    return {"message": "Hello World, this is server 2"}
