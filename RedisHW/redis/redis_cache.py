import redis
from redis_lru import RedisLRU


client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def f(x, y):
    match y:
        case 0:
            return 1
        case 1:
            return x
        case n:
            return x * f(x, y - 1)


if __name__ == '__main__':
    x = int(input('Pls, enter x: '))
    y = int(input('Pls, enter y: '))
    result = f(x, y)
    print(f'{x}^{y} = {result}')

