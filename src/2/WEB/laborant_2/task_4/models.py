from pydantic import BaseModel, Field, field_validator
import re

class User(BaseModel):
    name: str
    age: int

class Feedback(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    message: str = Field(min_length=10, max_length=500)
    
    @field_validator('message')
    @classmethod
    def validate_message(cls, message: str) -> str:
        forbidden_words = ["редиска", "бяка", "козявка"]
        message_lower = message.lower()
        for forbidden_word in forbidden_words:
            pattern = rf'\b{forbidden_word[:-2]}[\w]*\b'
            if re.search(pattern, message_lower):
                raise ValueError("Использование недопустимых слов")
        return message