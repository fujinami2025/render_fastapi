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
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HTMLの基本構造</title>
</head>
<body>

<!-- 見出しの例 -->
<h1>これは見出し1です</h1>
<h2>これは見出し2です</h2>

<!-- 段落の例 -->
<p>これは段落です。段落タグを使ってテキストをまとめます。</p>

<!-- リンクの例 -->
<p>こちらは<a href="https://example.com">リンク</a>です。クリックすると他のページに移動します。</p>

</body>
</html>
    """
    return HTMLResponse(content=html_content, status_code=200)

class PresentRequest(BaseModel):
    present: str

@app.post("/present")
async def give_present(present):
    return {"response": f"(from server)ハッピーハロウィン！ Thank you for"{present}"I'll return candy."}
