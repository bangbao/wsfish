# coding: utf-8

import datetime
import hashlib
import MySQLdb

md5 = lambda x: hashlib.md5(x).hexdigest()
escape_string = MySQLdb._mysql.escape_string


def force_str(text, encoding="utf-8", errors='strict'):
    t_type = type(text)
    if t_type == str:
        return text
    elif t_type == unicode:
        return text.encode(encoding, errors)
    return str(text)

def _smart(v):
    t = type(v)
    if t == str:
        return v
    elif t == unicode:
        return force_str(v)
    elif (t == int) or (t == long) or (t == float):
        return str(v)
    elif t == datetime.datetime:
        return v.strftime("%Y-%m-%d %H:%M:%S")
    return str(v)


def sql_value(dict_data):
    return ','.join(map(
        lambda x: """%s='%s'""" % (
            x[0], escape_string(_smart(x[1])) if x[1] is not None else 'null'
        ),
        dict_data.iteritems()
    ))


class MySQLConnect(object):
    """mysql"""
    def __init__(self, host_config):
        self.mysql_host = host_config
        self.table_prefix = host_config['table_prefix']
        self.conn = MySQLdb.connect(
            host=host_config['host'],
            user=host_config['user'],
            passwd=host_config['passwd'],
            db=host_config['db'],
            charset="utf8"
        )
        self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)

    def __enter__(self,):
        return self

    def __exit__(self, _type, value, trace):
        pass
#         self.cursor.close()
#         self.conn.close()

    def __del__(self,):
        self.conn.close()
        self.cursor.close()

    def get_table_by_key(self, key):
        """根据key取出所在的table
        """
        sid = int(md5(str(key)), 16)
        table = '%s_%s' % (self.table_prefix, sid % 16)
        return table

    def execute(self, sql, key):
        table = self.get_table_by_key(key)
        sql = sql % table
        self.cursor.execute(sql)
        self.conn.commit()

    def insert_data(self, data, key):
        sql = """INSERT INTO %s SET """ + sql_value(data)
        return self.execute(sql, key)


