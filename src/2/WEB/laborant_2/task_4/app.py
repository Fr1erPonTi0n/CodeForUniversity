from fastapi import FastAPI
from models import User, Feedback
from typing import List

app = FastAPI()

feedback_storage: List[Feedback] = []

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

@app.post("/feedback")
def submit_feedback(feedback: Feedback):
    feedback_storage.append(feedback)
    return {
        "message": f"Feedback received. Thank you, {feedback.name}."
    }

@app.get("/feedbacks")
def get_all_feedbacks():
    return {
        "feedbacks": feedback_storage,
        "count": len(feedback_storage)
    }