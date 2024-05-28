from fastapi import FastAPI, BackgroundTasks, Request
from pydantic import BaseModel
import httpx
import asyncio

class PongTime(BaseModel):
    pong_time: int

app = FastAPI()
pong_time_ms = 1000
is_running = False
pause_event = asyncio.Event()

@app.get("/ping")
async def ping():
    return "pong"

@app.post("/control/start")
async def start_game(pong_time: PongTime, background_tasks: BackgroundTasks):
    global pong_time_ms, is_running
    pong_time_ms = pong_time.pong_time
    is_running = True
    pause_event.set()
    background_tasks.add_task(ping_pong_loop)
    return {"status": "started", "pong_time_ms": pong_time_ms}

@app.post("/control/pause")
async def pause_game():
    global is_running
    is_running = False
    pause_event.clear()
    return {"status": "paused"}

@app.post("/control/resume")
async def resume_game():
    global is_running
    is_running = True
    pause_event.set()
    return {"status": "resumed"}

@app.post("/control/stop")
async def stop_game():
    global is_running
    is_running = False
    return {"status": "stopped"}

async def ping_pong_loop():
    while is_running:
        await pause_event.wait()
        await ping_server("http://localhost:8000/ping")
        await asyncio.sleep(pong_time_ms / 1000)

async def ping_server(url: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            if response.text == "pong":
                print(f"Received pong from {url}")
        except httpx.RequestError as exc:
            print(f"An error occurred while requesting {exc.request.url!r}.")
