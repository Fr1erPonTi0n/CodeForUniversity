from redis import Redis
from abc import ABC
from core import config

class RedisTokensHelper(ABC):
    def __init__(self, port, host, db, set_name_tokens):
        self.redis = Redis(
            port=port,
            host=host,
            db=db,
            decode_responses=True
        )
        self.tokens_name = set_name_tokens

    def token_exists(self, token: str) -> bool:
        return bool(
            self.redis.sismember(
                self.tokens_name,
                token,
            )
        )
    
    def add_token(self, token: str) -> bool:
        self.redis.sadd(self.token_exists, token)


redis_tokens = RedisTokensHelper(
    port=config.REDIS_PORT,
    host=config.REDIS_HOST,
    db=config.REDIS_DB_TOKENS,
    set_name_tokens=config.REDIS_TOKENS_SET_NAME
)