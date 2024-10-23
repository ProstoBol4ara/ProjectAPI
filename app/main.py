from controllers import router
from fastapi import FastAPI

app = FastAPI()

app.include_router(router=router)

@app.get("/")
async def main():
    return {"Welcome!": "This is FAST mb API"}