# coding: utf-8

import json
import itertools
from . import consts


mapping = {
    "int": lambda x: int(float(x)) if x not in (None, '', 'null') else 0,
    "float": lambda x: float(x) if x not in (None, '', 'null') else 0.0,
    "str": lambda x: str(x) if x is not None else '',
    "unicode": lambda x: unicode(x) if x is not None else u'',
    'int_list': lambda x: [int(float(i)) for i in str(x).split(',') if i],
    'float_list': lambda x: [float(i) for i in str(x).split(',') if i],
    'str_list': lambda x: [str(i) for i in x.split(',')],
    'unicode_list': lambda x: [unicode(i) for i in x.split(',')],
    'json': lambda x: json.loads(x) if x else '',
    'eval': lambda x: eval(x, {}, {}) if x else None,
}


def yield_xlrd_to_pyobj(s):
    """xlrd表转换成python字典数据
    """
    # 第一行为字段key
    keys = [k.strip() for k in s.row_values(0)]
    # 第二行是否真实内容， 一般第一列为数字类型
    start_n = 1
    row2 = s.row_values(1)
    if not isinstance(row2[0], (int, float)):
        start_n = 2
    # 内容开始
    for i in xrange(start_n, s.nrows):
        row = s.row_values(i)
        if row[0] is None or row[0] == '':
            continue
        d = dict(itertools.izip(keys, row))
        yield d


def xls_to_config(config_name, xls_data):
    """xlrd表转换成配置数据
    """
    row_template = consts.CONFIG_TEMPLATES[config_name]

    r = {}
    for n, row in enumerate(xls_data):
        d = {}
        for key, keymap in row_template.iteritems():
            xkey, xfunc = keymap[:2]
            if isinstance(xkey, basestring):
                func = mapping[xfunc]
                try:
                    d[key] = func(row[xkey])
                except Exception as e:
                    print('ERRORKEY: %s.%s %s' % (config_name, xkey, row[xkey]))
            elif isinstance(xkey, (tuple, list)):
                func = mapping[xfunc]
                d[key] = func(xkey, row)
            else:
                print 'ERRORKEY: %s.%s' % (config_name, xkey)
                continue
        pk = d.pop('pk', None)
        if pk is not None:
            r[pk] = d
        else:
            r = d
    return r
