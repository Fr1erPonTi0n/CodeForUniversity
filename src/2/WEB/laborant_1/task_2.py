from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
import os

app = FastAPI()

@app.get("/")
async def root():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(current_dir, "index.html")
    return FileResponse(file)

if __name__ == "__main__":
    uvicorn.run("task_2:app", reload=True)
    