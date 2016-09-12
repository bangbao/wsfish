# coding: utf-8

import time
import random
import string

BASE_USER_SEQ = [97, 97, 97, 0, 0, 0]
USER_SEQ_FACTOR = [26 * 26 * 1000, 26 * 1000, 1000, 100, 10]

chars = string.digits + string.ascii_uppercase + string.ascii_lowercase
chars_len = len(chars)

def salt_generator(size=6):
    return ''.join(random.choice(chars) for _ in xrange(size))


def trans_uid(uid_num, server_token='', unique_token=''):
    """将数字转换为字母串
    args:
        uid_num: 数字ID
        server_token: 分服标识ID
        unique_token: 平台标识ID
    returns:
        字母串: a00aaa001
    """
    seqs = [unique_token, server_token]
    shang, mod = 0, int(uid_num)

    for i, factor in enumerate(USER_SEQ_FACTOR):
        shang, mod = divmod(mod, factor)

        if i < 3:
            seqs.append(chr(shang + BASE_USER_SEQ[i]))
        else:
            seqs.append(str(shang + BASE_USER_SEQ[i]))

    seqs.append(str(mod))

    return ''.join(seqs)


def decompress_uid(uid):
    """ 把uid转换成数字
    args:
        uid: 用户6位ID(aaa001)
    returns:
        转换后的数字
    """
    number = 0

    for i in xrange(0, 5):
        if i < 3:
            factor = ord(uid[i])
        else:
            factor = int(uid[i])

        number += (factor - BASE_USER_SEQ[i]) * USER_SEQ_FACTOR[i]

    i += 1
    number += int(uid[i])

    return number


def int_to_str62(num):
    """把整形转换成62进制的串
    Args:
        num: 整数
    Returns:
        62进制的串
    """
    res = []
    while num > 0:
        num, asc = divmod(num, chars_len)
        res.append(chars[asc])

    res = reversed(res)
    return ''.join(res)


def str62_to_int(str62):
    """把62进制的串转换成整形
    Args:
        str62: 串
    Returns:
        num: 整形
    """
    num = 0
    for s in str62:
        idx = chars.find(s)
        if idx >= 0:
            num = num * chars_len + idx
    return num


def timestamp_to_str62(timestamp=None):
    """时间戳转换到62进制
    Args:
        timestamp: 时间戳，不传默认当前时间
    Returns:
        62进制串
    """
    timestamp = timestamp or time.time()
    timestamp = int(timestamp)

    return int_to_str62(timestamp)


if __name__ == '__main__':
    print salt_generator()
    print 'b00abc123:', trans_uid(28123, '00', 'b')
    print 'abc123:', decompress_uid('abc123')
    x = 28123
    s = int_to_str62(x)
    y = str62_to_int(s)
    print( x , s , y)
    print timestamp_to_str62()



