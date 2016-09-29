# coding: utf-8

import json
import itertools
from . import consts


mapping = {
    "int": lambda x: int(float(x)) if x else 0,
    "float": lambda x: float(x) if x else 0.0,
    "str": lambda x: str(x) if x is not None else '',
    "unicode": lambda x: unicode(x) if x is not None else u'',
    'int_list': lambda x: [int(float(i)) for i in str(x).split(',') if i],
    'float_list': lambda x: [float(i) for i in str(x).split(',') if i],
    'str_list': lambda x: [str(i) for i in x.split(',')],
    'unicode_list': lambda x: [unicode(i) for i in x.split(',')],
    'json': lambda x: json.loads(x) if x else '',

    # "list"              : lambda x: eval("""[%s]""" % x) if x is not None else"""[]""",     # 可能有多层的数据结构 eg:[1, [2, 3], 4]
    # "single_list"       : lambda x: eval("""%s""" % x) if x is not None else"""[]""", # 只有一层的数据结构 eg:[1, 2]
    # "int_single_list"   : lambda x: [int(i) for i in eval("""[%s]""" % x)] if x is not None else"""[]""", # 只有一层的数据结构 eg:[1, 2]
    # "str_list"          : lambda x: str([str(i) for i in str(x).split(',')]) if x is not None else """[]""",
    # "unicode_list"      : lambda x: unicode([i for i in x.split(',')]) if x else """[]""",
    # "unicode_int_list"  : lambda x: adv_unicode_int_list(x) if x is not None else"""[]""",
    # 'int_0_list'        : lambda x: eval("""[%s]""" % x) if x else """[0]""",
}


def yield_xlrd_to_pyobj(s):
    """
    """
    # 第一行为字段key
    keys = s.row_values(0)

    for i in xrange(1, s.nrows):
        row = s.row_values(i)
        if row[0] is None:
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
        for key, (xkey, xfunc) in row_template.iteritems():
            if isinstance(xkey, basestring):
                func = mapping[xfunc]
                d[key] = func(row[xkey])
            elif isinstance(xkey, (tuple, list)):
                func = mapping[xfunc]
                d[key] = func(xkey, row)
            else:
                print 'error xkey: %s %s' % (config_name, xkey)
                continue
        pk = d.pop('pk', None)
        if pk is not None:
            r[pk] = d
        else:
            r = d
    return r

def to_config_string(config_name, data, filepath):
    """# to_config_string: docstring
    args:
        data:    ---    arg
        filepath:    ---    配置xlsx路径
    returns:
        0    ---
    """
    return_data = getattr(CT, config_name)()
    if len(return_data) == 2:
        # 普通结构
        t, funcs = return_data
    else:
        # 特殊结构
        t, funcs, especial = return_data
        return to_config_string_special(config_name, data, filepath, t, funcs)

    r = []
    for row, v in enumerate(data):
        for tt in t:
            vv = None
            #if tt[0] != 'END' and tt[0] not in v:
            #    continue
            try:
                if tt[2] == 'None':
                    s = tt[1]
                elif isinstance(tt[2],tuple):
                    l = []
                    for i in xrange(len(tt[2])):
                        if isinstance(tt[0], tuple):
                            vv = v[tt[0][i]]
                        else:
                            vv = v[tt[0]+'_'+str(i)]
                        l.append(mapping[tt[2][i]](vv))
                    s = tt[1]%tuple(l)
                else:
                    vv = v[tt[0]]
                    s = tt[1]%mapping[tt[2]](vv)
            except Exception as e:
                _, filename = os.path.split(filepath)
                err_msg = '%s, %s-%s %r: %r, %r, %r' % (filename, config_name, row+2, e, tt[0], vv, tt[2])
                print err_msg
                raise Exception(err_msg)
            if funcs.get(tt[0], lambda x: True)(v):
                r.append(s)
            del tt
    return '{\n'+'\n'.join(r)+'\n}'

