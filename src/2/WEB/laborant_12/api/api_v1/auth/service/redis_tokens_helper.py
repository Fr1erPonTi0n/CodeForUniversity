from redis import Redis
from tokens_helper import AbstractTokensHelper
from core import config

class RedisTokensHelper(AbstractTokensHelper):
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
        return self.redis.sadd(self.token_exists, token)

    def delete_token(self, token: str) -> bool:
        return bool(self.redis.srem(self.tokens_name, token))
    
    def get_tokens(self) -> list[str]:
        return list(self.redis.smembers(self.tokens_name))


redis_tokens = RedisTokensHelper(
    port=config.REDIS_PORT,
    host=config.REDIS_HOST,
    db=config.REDIS_DB_TOKENS,
    set_name_tokens=config.REDIS_TOKENS_SET_NAME
)