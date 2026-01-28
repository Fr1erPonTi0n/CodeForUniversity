from fastapi import FastAPI
from models import User

app = FastAPI()

user = User(name="John Doe", id=1)

users_list = [user]

@app.get("/users")
def get_users():
    return {
        "users": users_list,
        "count": len(users_list)
    }
