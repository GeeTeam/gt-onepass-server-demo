from time import time

from Cryptodome.Hash import SHA256, HMAC


def hmac_sha256_sign(secret, key: bytes):
    h = HMAC.new(key, digestmod=SHA256)
    h.update(secret.encode())
    return h.hexdigest()


def gen_sign(app_id, app_key, timestamp):
    secret = app_id + '&&' + timestamp
    sign = hmac_sha256_sign(secret, app_key.encode())
    return sign


if __name__ == '__main__':
    app_id, app_key = 'zoekwui1hnmg49x5fwzf5la0ml5dziwn', 'gywzffojtnzl0vd6kcut8fcgyud5wg49'
    timestamp = str(int(time() * 1000))
    # timestamp = '1542355862990'

    res = gen_sign(app_id, app_key, timestamp)
    print(res)
