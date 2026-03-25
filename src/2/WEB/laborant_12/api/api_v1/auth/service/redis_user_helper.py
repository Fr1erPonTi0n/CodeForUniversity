from .users_helper import AbstractUserHelper
from core import config
from redis import Redis


class RedisUsersHelper(AbstractUserHelper):
    def __init__(
        self,
        port: int,
        host: str,
        db: int
    ):
        self.redis = Redis(
            port=port,
            host=host,
            db=db,
            decode_responses=True
        )

    def get_user_password(self, username):
        return self.redis.get(f"users:{username}")
    
redis_users = RedisUsersHelper(
    port=config.REDIS_PORT,
    host=config.REDIS_HOST,
    db=config.REDIS_DB_USERS
)
    
