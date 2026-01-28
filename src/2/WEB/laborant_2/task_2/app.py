from fastapi import FastAPI
from models import User

app = FastAPI()

user = User(name="John Doe", age=17)

users_list = [user]

@app.get("/users")
def get_users():
    return {
        "users": users_list,
        "count": len(users_list)
    }

@app.post("/user")
def check_user_age(user: User):
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": user.age >= 18
    }
