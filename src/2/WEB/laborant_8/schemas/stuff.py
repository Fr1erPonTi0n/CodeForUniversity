from redis import Redis
from core import REDIS_PORT, REDIS_DB, REDIS_HOST

r = Redis(
    port=REDIS_PORT,
    host=REDIS_HOST,
    db=REDIS_DB,
)

def main():
    print(r.ping())
    print(r.get("name"))
    print(r.get('foo'))
    print(r.set("foo", "bar"))
    print(r.get("foo"))
    print(r.keys())


main()