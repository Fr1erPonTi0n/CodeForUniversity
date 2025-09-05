import re
from typing import List


# 1 ЗАДАНИЕ
def is_valid_email(email: str) -> bool:
    pattern = r'^[\w.]+@[a-z.]+\.[a-z]{2,6}$'
    return bool(re.match(pattern, email))


print(is_valid_email('john_doe@example.com'))
print(is_valid_email('user.name@domain.co.uk'))


# 2 ЗАДАНИЕ
def extract_dates(text: str) -> List[str]:
    pattern = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    return re.findall(pattern, text)


print(extract_dates("Встреча 12-04-2023 и потом 15/05/2024"))


# 3 ЗАДАНИЕ
def mask_numbers(text: str) -> str:
    pattern = r'\b\d+\.?\d*\b'
    return re.sub(pattern, '<num>', text)


print(mask_numbers('У него было 5 яблок и 3.14 пирога'))


# 4 ЗАДАНИЕ
def is_strong_password(password: str) -> bool:
    if len(password) < 8 or len(password) > 20:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[@#$%^&+=.]', password):
        return False
    return True


print(is_strong_password('Short1@'))
print(is_strong_password('weakpassword'))
print(is_strong_password('StringPass1@'))


# 5 ЗАДАНИЕ
def extract_tags(html: str) -> List[str]:
    pattern = r'<\/?([a-zA-Z0-9]+)(?:>|\/)'
    return re.findall(pattern, html)


print(extract_tags('<div><p>Hello</p><br/></div>'))


# 6 ЗАДАНИЕ
def find_repeated_words(text: str) -> List[str]:
    pattern = r'\b(\w+)\s+\1\b'
    matches = re.findall(pattern, text)
    return list(dict.fromkeys(matches))


print(find_repeated_words("This is is a test test test string"))


# 7 ЗАДАНИЕ
def split_words(text: str) -> List[str]:
    return re.findall(r'\b[\w\-]+\b', text)


print(split_words("Hello, world! How are you?"))
