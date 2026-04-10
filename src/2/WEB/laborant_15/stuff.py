from redis import Redis

from core import config

r = Redis(
    port=config.REDIS_PORT,
    host=config.REDIS_HOST,
    db=config.REDIS_DB,
)


def main():
    print(r.ping())
    print(r.get("name"))
    print(r.get("foo"))
    print(r.set("foo", "bar"))
    print(r.get("foo"))
    print(r.keys())


main()
