# https://open.feishu.cn/document/client-docs/bot-v3/add-custom-bot#272b1dee

import time

import hashlib
import base64
import hmac


def get_now_timestamp() -> int:
    return int(time.time())


def gen_sign(timestamp: int, secret: str) -> str:
    # 拼接timestamp和secret
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    hmac_code = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()

    # 对结果进行base64处理
    sign = base64.b64encode(hmac_code).decode('utf-8')

    return sign


def get_sign(secret: str) -> str:
    timestamp = get_now_timestamp()
    sign = gen_sign(timestamp, secret)
    return sign


class FeiShuBot:
    pass


if __name__ == "__main__":
    print(get_now_timestamp())
