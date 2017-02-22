# coding: utf-8

from . import hooks as h

CONFIG_LIST = (
    # (key, sheet_name, hook_funcs, send_client)
    ('resource_versions',       None,               None,                   0),
    ('resource_update',         None,               None,                   0),
    ('servers',                 None,               h.servers_f,            0),
    ('serverctrl',              'serverctrl',       None,                   0),
    ('text_warning',            'text_warning',     None,                   0),
    ('month_gift',              'month_gift',       None,                   1),
)

SHEET_CONFIG_MAP = dict((i[1], i[0]) for i in CONFIG_LIST)
CONFIG_TEMPLATES = {
    'award_sp': {
        'pk': ('id', 'int'),
        'id': ('sort', 'int'),
        'list': ('list', 'int_list'),
        'float': ('float', 'float'),
        'json': ('json', 'json'),
    },
}
