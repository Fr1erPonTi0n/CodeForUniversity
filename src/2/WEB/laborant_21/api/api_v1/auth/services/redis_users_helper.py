from .users_helper import AbstractUserHelper
from redis import Redis
from core import config


class RedisUsersHelper(AbstractUserHelper):
    def __init__(
        self,
        port: int,
        host: str,
        db: int,
    ):
        self.redis = Redis(
            port=port,
            host=host,
            db=db,
            decode_responses=True,
        )

    def get_user_password(
        self,
        username: str,
    ) -> str | None:
        return self.redis.get(username)


redis_users = RedisUsersHelper(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB_USERS,
)
