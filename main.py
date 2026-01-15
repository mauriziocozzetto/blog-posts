from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import json
import os

app = FastAPI()

# Percorso del file JSON creato in precedenza
JSON_FILE = "posts.json"


@app.get("/api/posts")
async def get_posts():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"error": "File non trovato"}

# Rotta per servire la pagina principale


@app.get("/")
async def read_index():
    return FileResponse('index.html')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
