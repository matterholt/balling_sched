from fastapi import FastAPI

from .routes.schedules import router as schedulesRoute




app = FastAPI()


@app.get("/")
async def root ():
    return {"message": "Hello world"}
