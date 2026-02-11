import uvicorn
from fastapi import FastAPI

from api import router as api_router

app = FastAPI(title="Books and Movies API")
app.include_router(api_router)

@app.get("/")
def read_root():
    return {
        "docs": "/docs",
        "api_v1": "/api/v1",
    }

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)



