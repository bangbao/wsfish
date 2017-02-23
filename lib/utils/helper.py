# coding: utf-8

import time
import random
import hashlib
import json
import string

BASE_USER_SEQ = [97, 97, 97, 0, 0, 0]
USER_SEQ_FACTOR = [26 * 26 * 1000, 26 * 1000, 1000, 100, 10]

sys_random = random.SystemRandom()
chars = string.digits + string.ascii_uppercase + string.ascii_lowercase
chars_len = len(chars)


def random_chars(size=6):
    """生成随机串
    """
    return ''.join(random.choice(chars) for _ in xrange(size))


def random_digits(size=7):
    """生成随机数字， 第一位不为0
    """
    digits = ([random.choice(string.digits[1:])] +
              [random.choice(string.digits) for _ in xrange(size)])
    return int(''.join(digits))


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


def trans_ip2number(ip):
    """把ip格式转换成数字， 三位数补齐
    """
    numbers = ('%03d' % int(number) for number in ip.split('.'))
    return int(''.join(numbers))


def trans_number2ip(number):
    """还原数字->ip
    """
    strip = str(number)
    numbers = (str(int(strip[index:index+3])) for index in xrange(0, len(strip), 3))
    return '.'.join(numbers)


def random_hit(probability):
    """ 判断概率是否命中
    随机0-100判断当前指定的概率是否符合要求
    Args:
        probability: 指定概率
    Returns:
        bool
    """
    return sys_random.randint(1, 100) <= probability


def dict_md5(data):
    datastr = json.dumps(data, sort_keys=True)
    return hashlib.md5(datastr).hexdigest()

def make_version(data):
    return dict_md5(data)


def weight_choice(goods, index=-1):
    """根据权重选出物品
    Args:
        goods: 物品列表，[('a', 10), ('b', 20), ('c', 30)]
        index: 指定权重数字在数组中的位置
    Returns:
        item: 选中的物品 ('b', 20)
    Raises:
        ValueError('goods can not be empty')
    """
    goods = sorted(goods, key=lambda x: x[index])
    weights = sum(data[index] for data in goods)
    weight = sys_random.uniform(0, weights)
    temp_weight = 0

    for item in goods:
        temp_weight += item[index]
        if temp_weight >= weight:
            return item
    raise ValueError('goods can not be empty')


def yield_weight_choice_repeat(goods, num, index=-1):
    """根据权重选出物品, 可重复
    Args:
        goods: 物品列表，[('a', 10), ('b', 20), ('c', 30)]
        num: 要选出的个数
        index: 指定权重数字在数组中的位置
    Yields:
        item: 选中的物品 ('b', 20)
    """
    goods = sorted(goods, key=lambda x: x[index])
    weights = sum(data[index] for data in goods)

    for _ in xrange(num):
        weight = sys_random.randint(1, weights)
        temp_weight = 0
        for item in goods:
            temp_weight += item[index]
            if temp_weight >= weight:
                yield item
                break


def yield_weight_choice_sample(goods, num, index=-1):
    """根据权重选出物品， 不可重复
    Args:
        goods: 物品列表，[('a', 10), ('b', 20), ('c', 30)]
        num: 要选出的个数
        index: 指定权重数字在数组中的位置
    Yields:
        item: 选中的物品 ('b', 20)
    """
    goods = sorted(goods, key=lambda x: x[index])
    weights = sum(data[index] for data in goods)

    for _ in xrange(num):
        weight = sys_random.randint(1, weights)
        temp_weight = 0
        for i, item in enumerate(goods):
            temp_weight += item[index]
            if temp_weight >= weight:
                yield item
                goods.pop(i)
                weights -= item[index]
                break


def to_json(obj):
    """将一些特殊类型转换为json
    """
    if isinstance(obj, set):
        return list(obj)
    if isinstance(obj, unicode):
        return obj.encode('utf-8')
    raise TypeError(repr(obj) + ' is not json seralizable')


def merge_dict(dict_a, dict_b):
    """合并两个字典, 现只对元素为数字和列表合并
    Args:
        dict_a: 字典a
        dict_b: 字典b
    Returns:
        dict_a: 合并后的字典a
    """
    for k, v in dict_b.iteritems():
        if k not in dict_a:
            dict_a[k] = v
        elif isinstance(v, int):
            dict_a[k] += v
        elif isinstance(v, list):
            dict_a[k].extend(v)
        elif isinstance(v, dict):
            merge_dict(dict_a[k], v)
        else:
            raise 'only merge element`s type are int and list'

    return dict_a


def merge_dict_value2list(a_dict, b_dict):
    """合并两个字典， value组成list
    Args:
        a_dict: 字典a
        b_dict: 字典b
    Returns:
        合并后的字典
    """
    new_dict = {}

    for k, v in a_dict.iteritems():
        new_dict[k] = (v, b_dict[k])

    return new_dict


def mktimestamp(timestr, fmt='%Y-%m-%d %H:%M:%S'):
    """转换时间字符串到时间戳
    Args:
        timestr: 时间字符串
        fmt: 对应的时间格式
    Returns:
        时间戳
    """
    struct_time = time.strptime(timestr, fmt)
    return int(time.mktime(struct_time))


def strftimestamp(timestamp, fmt='%Y-%m-%d %H:%M:%S'):
    """转换时间戳到字符串
    Args:
        timestamp: 时间戳
        fmt: 对应的时间格式
    Returns:
        时间字符串
    """
    struct_time = time.localtime(timestamp)
    return time.strftime(fmt, struct_time)


def dt2timestamp(dt):
    """转换日期时间对象到时间戳
    Args:
        dt: datetime.datetime()对象
    Returns:
        时间戳
    """
    struct_time = dt.timetuple()
    return int(time.mktime(struct_time))


def generate_rank_score(score, now=None):
    """ 生成排名的积分
    Args:
        score: 需要转换的积分
        now: 当前的时间搓
    Returns:
        score: 排名积分
    """
    now = now or time.time()
    return score + 1 - now / 10 ** 10


def round_float_or_str(num, func=int):
    """ 数据向上取整
    Args:
        num: 需要转换的数据(float|str)
    Returns:
        int: 返回的整数
    """
    return func(round(float(num)))


def int_float_or_str(num, func=int):
    """ 数据向上取整
    Args:
        num: 需要转换的数据(float|str)
    Returns:
        int: 返回的整数
    """
    return func(float(num))


def get_member_data(data, rank_start=1, num=10):
    """获取指定的n条数据
    Args:
        data: 数据内容(list结构)
        rank_start: 获取当前及后面的n个数据
        num: 每次获取n条数据
    """
    start_idx = rank_start-1
    end_idx = start_idx + num

    if len(data) < start_idx:
        return []

    if len(data) < end_idx:
        return data[start_idx:]

    return data[start_idx:end_idx]


if __name__ == '__main__':
    print random_chars()
    print 'b00abc123:', trans_uid(28123, '00', 'b')
    print 'abc123:', decompress_uid('abc123')
    x = 28123
    s = int_to_str62(x)
    y = str62_to_int(s)
    print( x , s , y)
    print timestamp_to_str62()
