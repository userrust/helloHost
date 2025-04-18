from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Монтируем статические файлы (HTML/CSS/JS)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_root():
    return {"message": "Добро пожаловать в FastBank API!11"}


@app.post("/api")
async def transfer_money():
    # Здесь была бы логика перевода
    return {"status":"success"}
