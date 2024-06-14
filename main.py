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
    omikuji_messages = [
        "大吉！素晴らしい幸運が舞い込むでしょう。",
        "中吉！努力が実を結び、良い結果が待っています。",
        "小吉！ちょっとした幸運があなたの元にやってきます。",
        "吉！安定した幸せな日々が続くでしょう。",
        "半吉！まずまずの運勢です。良いことも悪いこともあります。",
        "末吉！努力が実り始め、良い方向に進む時期です。",
        "末小吉！運気が上向きになってきています。良いことが起こるかもしれません。",
        "凶。悪いことが起こるかもしれませんが、気を引き締めてください。",
        "小凶。注意が必要な日です。慎重に行動しましょう。",
        "大凶。厳しい状況が訪れるかもしれませんが、乗り越えましょう。"
    ]

    omikuji_index = random.randrange(10);
    return {
        "result": omikuji_list[omikuji_index],
        "message": omikuji_messages[omikuji_index]
    }

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