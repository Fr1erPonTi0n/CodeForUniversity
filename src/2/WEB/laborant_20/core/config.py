from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
REDIS_PORT = 6379
REDIS_HOST = "localhost"
REDIS_DB = 0
REDIS_DB_TOKENS = 1
REDIS_DB_USERS = 2
REDIS_DB_BOOKS = 3 

REDIS_SET_NAME_TOKENS = "tokens"
REDIS_HASH_NAME_BOOKS = "books"
