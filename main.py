from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Монтируем статические файлы (HTML/CSS/JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    return {"message": "Добро пожаловать в FastBank API!"}

@app.get("/api/balance")
async def get_balance():
    return {"balance": 10000, "currency": "RUB"}

@app.post("/api/transfer")
async def transfer_money(amount: float, recipient: str):
    # Здесь была бы логика перевода
    return {"status": "success", "message": f"Переведено {amount} RUB пользователю {recipient}"}