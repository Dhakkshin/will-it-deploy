from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from a fastapi app hosted on vercel", "status": "ok"} 

@app.get("/ping")
async def ping():
    return {"status": "ok", "message": "pong"}
