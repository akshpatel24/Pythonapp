from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.post("/items/{name}", status_code=201)
async def create_item(name: str):
    return {"name": name}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)