# coding: utf-8


class PY2LUA(object):
    """trans python object to lua object
    """
    number_types = (int, float, long, complex)
    bool_types = (bool,)
    string_types = (basestring,)
    table_array_types = (tuple, list)
    table_dict_types = (dict,)

    escape = {
        '"': "'",
        # '/': '\\/',
        '\\': '\\\\',
        '\b': '\\b',
        '\f': '\\f',
        '\n': '\\n',
        '\r': '\\r',
        '\t': '\\t',
    }

    def __init__(self):
        self.depth = 0
        self.tab = '\t'
        self.newline = '\n'

    def escape_string(self, obj):
        s = (self.escape.get(ch, ch) for ch in obj)
        return ''.join(s)

    def encode(self, obj):
        self.depth = 0
        return self._encode(obj)

    def _encode(self, obj):
        if obj is None:
            return 'nil'

        if isinstance(obj, self.bool_types):
            return str(obj).lower()

        if isinstance(obj, self.number_types):
            return str(obj)

        if isinstance(obj, self.string_types):
            return '"%s"' % self.escape_string(obj)

        if isinstance(obj, self.table_array_types):
            s = []
            s.append("{" + self.newline)
            self.depth += 1
            for el in obj:
                s.append(self.tab * self.depth + self._encode(el) + ',' + self.newline)
            self.depth -= 1
            s.append(self.tab * self.depth + "}")
            return ''.join(s)

        if isinstance(obj, self.table_dict_types):
            s = []
            s.append("{" + self.newline)
            self.depth += 1
            for key, value in obj.iteritems():
                s.append(self.tab * self.depth + ('["%s"]' % key) + ' = ' + self._encode(value) + ',' + self.newline)
            self.depth -= 1
            s.append(self.tab * self.depth + "}")
            return ''.join(s)


if __name__ == '__main__':
    py2lua = PY2LUA()
    data = {'list': [{'cnname': u'\u65e0\u540d\u58eb23', 'id': 12}, 12, 'string'], 'tuple': (1, 2, [3,4], {1: 2}), 'number': 12.0, 'dict': {'a': 1}}
    result = py2lua.encode(data)
    print result.encode('utf-8')
