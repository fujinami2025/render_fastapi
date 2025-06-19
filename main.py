from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉", "中吉", "小吉", "吉", "半吉",
        "末吉", "末小吉", "凶", "小凶", "大凶"
    ]
    return {"result": random.choice(omikuji_list)}

@app.get("/index")
def index():
    html_content = """
    <html>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
    <title>阿部寛のホームページ</title>
    </head>
    <frameset cols=18,82>
      <frame src="menu.htm" name="left">
      <frame src="top.htm" name="right">
      <noframes>
      <body></body>
      </noframes>
    </frameset>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

class PresentRequest(BaseModel):
    present: str

@app.post("/present")
async def give_present(present):
    return {"response": f"サーバです。メリークリスマス！ {present}ありがとう。お返しはキャンディーです。"}
