from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

router = APIRouter()

@router.get("/w")
async def root():
    msg = "Welcome to PyBites' FastAPI Learning Path 🐍 🎉"
    return {"message": msg}


@router.get("/", response_class=HTMLResponse)
# https://stackoverflow.com/questions/65296604/how-to-return-a-htmlresponse-with-fastapi
async def read_items():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


    
@router.get("/tap")
async def root():
    msg = "tap test"
    return {"message": msg}