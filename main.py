import random
from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]
    return omikuji_list[random.randrange(10)]

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>今日の格言</title>
        </head>
        <body>
            <h1>今日の格言</h1>
            <h2>「行動することで、道が開ける。」 - ChatGPT</h2>
            <p>これは、どんなに小さな一歩でも、実際に行動することで新しい機会や可能性が広がることを示しています。<br>挑戦を恐れず、まずは一歩踏み出してみましょう。</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)