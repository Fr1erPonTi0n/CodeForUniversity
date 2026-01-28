from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def greet():
    return {
        "message": "Добро пожаловать в моё приложение FastAPI!",
    }

if __name__ == "__main__":
    uvicorn.run("task_1:app", reload=True)
    