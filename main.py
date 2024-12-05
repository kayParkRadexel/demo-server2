from fastapi import FastAPI

app = FastAPI()


@app.get("/service2/")
async def root():
    return "Hello World, this is server 2"


@app.get("/service2/be2", status_code=200)
async def be2():
    return "Hello World, this is server 2"
