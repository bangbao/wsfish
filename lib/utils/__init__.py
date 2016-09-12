# coding: utf-8

VERSION = (0, 0, 1)

import time
import datetime
import random
import hashlib

sys_random = random.SystemRandom()


def get_it(probability):
    """ 判断概率是否命中
    随机0-100判断当前指定的概率是否符合要求
    Args:
       probability: 指定概率
    Returns:
       是否命中
    """
    return sys_random.randint(1, 100) <= probability


def md5(s):
    return hashlib.md5(str(s)).hexdigest()


def dict_md5(data):
    sorted_items = sorted(data.iteritems())
    data_str = '&'.join('%s=%s' % (k,v) for k, v in sorted_items)

    return hashlib.md5(data_str).hexdigest()


def make_version(data):
    m = dict_md5(data)
    v1 = sum([int(ord(i))%16 for i in m])
    v2 = sum([int(ord(i))%15 for i in m])
    v3 = sum([int(ord(i))%14 for i in m])
    v4 = sum([int(ord(i))/2 for i in m])
    return str(v1+v2+v3+v4)


def weight_choice(goods, index=-1):
    """根据权重选出物品
    Args:
        goods: 物品列表，[('a', 10), ('b', 20), ('c', 30)]
        index: 指定权重数字在数组中的位置
    Returns:
        选中的物品 ('b', 20)
    """
    goods = sorted(goods, key=lambda x: x[index])
    weights = sum(data[index] for data in goods)
    weight = sys_random.randint(1, weights)
    temp_weight = 0

    for data in goods:
        temp_weight += data[index]
        if temp_weight >= weight:
            return data


def yield_weight_choice_repeat(goods, num, index=-1):
    """根据权重选出物品, 可重复
    Args:
        goods: 物品列表，[('a', 10), ('b', 20), ('c', 30)]
        num: 要选出的个数
        index: 指定权重数字在数组中的位置
    Yields:
        选中的物品 ('b', 20)
    """
    goods = sorted(goods, key=lambda x: x[index])
    weights = sum(data[index] for data in goods)

    for _ in xrange(num):
        weight = sys_random.randint(1, weights)
        temp_weight = 0
        for data in goods:
            temp_weight += data[index]
            if temp_weight >= weight:
                yield data
                break


def yield_weight_choice_sample(goods, num, index=-1):
    """根据权重选出物品， 不可重复
    Args:
        goods: 物品列表，[('a', 10), ('b', 20), ('c', 30)]
        num: 要选出的个数
        index: 指定权重数字在数组中的位置
    Yields:
        选中的物品 ('b', 20)
    """
    goods = sorted(goods, key=lambda x: x[index])
    weights = sum(data[index] for data in goods)

    for _ in xrange(num):
        weight = sys_random.randint(1, weights)
        temp_weight = 0
        for i, data in enumerate(goods):
            temp_weight += data[index]
            if temp_weight >= weight:
                yield data
                goods.pop(i)
                weights -= data[index]
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
        排名积分
    """
    now = now or time.time()
    return score + 1 - now / 10 ** 10


def round_float_or_str(num, func=int):
    """ 数据向上取整
    Args:
        num: 需要转换的数据(float|str)
    Returns:
        返回的整数
    """
    return func(round(float(num)))


def int_float_or_str(num, func=int):
    """ 数据向上取整
    Args:
        num: 需要转换的数据(float|str)
    Returns:
        返回的整数
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

