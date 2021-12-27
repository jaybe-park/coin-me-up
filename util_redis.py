import redis


def get_redis_connection(host='localhost', port=6379, db=0, encoding='utf-8', decode_responses=True):
    r = redis.StrictRedis(
        host='localhost',
        port=6379,
        db=0,
        encoding='utf-8',
        decode_responses=True
    )

    return r
