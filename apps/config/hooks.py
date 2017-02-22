# coding: utf-8


def servers_f(self, name, value):
    pass


def charge_f(self, name, value):
    """充值定单配置，额外增加商品id到配置的映射配置
    """
    data = {}
    open_gifts = {}
    for buy_id, obj in value.iteritems():
        data[obj['cost']] = buy_id
        open_gifts.setdefault(obj['open_gift'], []).append(buy_id)
    setattr(self, 'charge_scheme', data)
    setattr(self, 'charge_open_gift', open_gifts)


def user_info_f(self, name, value):
    rent_num_openlv = {}
    for level, obj in sorted(value.iteritems()):
        if obj['rent_num'] not in rent_num_openlv:
            rent_num_openlv[obj['rent_num']] = level
    setattr(self, 'rent_num_openlv', rent_num_openlv)
