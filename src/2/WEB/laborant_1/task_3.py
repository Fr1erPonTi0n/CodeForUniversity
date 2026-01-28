from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/calculate")
def add(num1: float, num2:float):
    return {
        "num1": num1,
        "num2": num2,
        "result": num1 + num2,
    }

if __name__ == "__main__":
    uvicorn.run("task_3:app", reload=True)
    