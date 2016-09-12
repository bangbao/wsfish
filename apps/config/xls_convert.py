# coding: utf-8

import os
import json
import itertools

import config_templates as CT


def unicode_int_list(x):
    l = x.split('],')
    r_l = []
    for ll in l:
        if not ll:
            continue
        ll = ll.strip(' ').replace(']', '').replace('[', '')
        llll = ll.split(',')
        try:
            r_l.append("""[unicode('''%s''', 'utf-8'), %s, %s]"""%tuple(llll))
        except:
            raise KeyError, str(llll)+ll
    return '['+','.join(r_l)+']'


def adv_unicode_int_list(x):
    ss = x.replace(' ', '').lstrip('[').rstrip(']')
    l = ss.split('],[')
    r = []
    for i in l:
        rr = [ii if ii.replace('.', '').isdigit() else 'unicode("""%s""", "utf-8")'%ii
              for ii in i.split(',')]
        r.append('['+ ', '.join(rr) +']')
    return '[' + ', '.join(r) + ']'


def adv_str(x):
    try:
        return """'%s'"""%str(x)
    except ValueError:
        return """'%s'"""%str(x)

def smart_list(x):
    try:
        return eval('[%s]' % x, {}, {})
    except NameError:
        return """'%s'""" % x.strip()

mapping = {
        "int"               : lambda x: int(float(x)) if x not in ['', ' ', None] else 0,
        "float"             : lambda x: float(x) if x not in ['', ' ', None] else 0.0,
        "str"               : lambda x: adv_str(x) if x is not None else """''""",
        "unicode"           : lambda x: """unicode('''%s''','utf-8')"""%x if x is not None else """''""",
        "bool"              : lambda x: """%s"""%bool(x) if x is not None else """False""",
        "list"              : lambda x: eval("""[%s]""" % x) if x is not None else"""[]""",     # 可能有多层的数据结构 eg:[1, [2, 3], 4]
        "single_list"       : lambda x: eval("""%s""" % x) if x is not None else"""[]""", # 只有一层的数据结构 eg:[1, 2]
        "int_single_list"   : lambda x: [int(i) for i in eval("""[%s]""" % x)] if x is not None else"""[]""", # 只有一层的数据结构 eg:[1, 2]
        "str_list"          : lambda x: str([str(i) for i in str(x).split(',')]) if x is not None else """[]""",
        "unicode_list"      : lambda x: unicode([i for i in x.split(',')]) if x else """[]""",
        "unicode_int_list"  : lambda x: adv_unicode_int_list(x) if x is not None else"""[]""",
        'int_0_list'        : lambda x: eval("""[%s]""" % x) if x else """[0]""",
        'json'              : lambda x: json.loads(x) if x else """''""",
}


def to_pyobj(s):
    """# to_pyobj: docstring
    args:
        s:    ---    arg
    returns:
        0    ---
    """
    r = []
    keys = []
    iter_r = s.iter_rows()
    for i, row in enumerate(iter_r):
        if i in [0]:
            for c in row:
                keys.append(c.internal_value)
            continue
        #if not row[0].internal_value: break
        is_None = True
        d = {}
        d['order'] = i  # 排序
        for k, v in itertools.izip(keys, row):
            if v.internal_value:
                is_None = False
            d[k] = v.internal_value
        if is_None:
            continue
        r.append(d)
    return r


def yield_xlrd_to_pyobj(s):
    """
    """
    # 第一行为字段key
    keys = s.row_values(0)

    for i in xrange(1, s.nrows):
        row = s.row_values(i)
        if row[0] is None: continue
        # if not any(row): continue
        d = dict(itertools.izip(keys, row))
        yield d


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



def to_config_string_special(config_name, data, filepath, t, funcs):
    """
    args:
        config_name:    ---    config_name
        data:    ---    arg
        filepath:    ---    配置xlsx路径
    returns:
        {
        'first_name':[],
        'middle_name':[],
        'last_name':[],
        }
    """
    new_data = {}
    for row, v in enumerate(data):
        # {'': u's', u'first_name': '', u'last_name': '', u'middle': ''}
        # 剔除key为''的数据
        if '' in v:
            v.pop('')
        if not any(v.values()):
            continue

        for tt in t:
            vv = None
            # ('first_name', "  'first_name'       : %s,", 'unicode')
            try:
                _key = tt[0]
                vv = v[tt[0]]
                if not vv:
                    continue

                value = eval(mapping[tt[2]](vv), {}, {})

                new_data.setdefault(_key, [])
                new_data[_key].append(value)

            except Exception as e:
                _, filename = os.path.split(filepath)
                err_msg = '%s, %s-%s %r: %r, %r, %r' % (filename, config_name, row+2, e, tt[0], vv, tt[2])
                print err_msg
                raise Exception(err_msg)

            del tt

    return repr(new_data)
