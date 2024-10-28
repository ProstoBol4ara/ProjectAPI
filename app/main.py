from controllers import router
from startup import app

app.include_router(router=router)

@app.get("/")
async def main():
    return {"Welcome!": "This is FAST mb API"}