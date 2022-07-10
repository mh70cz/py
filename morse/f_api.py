from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from routes import general

app = FastAPI()
app.include_router(general.router)


@app.get("/morse")
async def root():
    msg = "morse test"
    return {"message": msg}


"""
cd .\morse
uvicorn f_api:app --reload


"""       