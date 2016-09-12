# encoding: utf-8

def serverctrl():
    return [
        ('server_id', """'%02d': {""", 'int'),
        ('server_id',       """ 'cfg_id'        : '%02d', """, 'int'),
        ('first_pay',       """ 'first_pay'     : %s, """, 'str'),
        ('act_xfyl',        """ 'act_xfyl'      : %s, """, 'int_single_list'),
        ('xfyl_time',       """ 'xfyl_time'     : %s, """, 'str'),
        ('act_xldh',        """ 'act_xldh'      : %s, """, 'int_single_list'),
        ('xldh_time',       """ 'xldh_time'     : %s, """, 'str'),
        ('act_czyl',        """ 'act_czyl'      : %s, """, 'int_single_list'),
        ('czyl_time',       """ 'czyl_time'     : %s, """, 'str'),
        ('act_xscj',        """ 'act_xscj'      : %s, """, 'int_single_list'),
        ('xscj_time',       """ 'xscj_time'     : %s, """, 'str'),
        ('act_jjyl',        """ 'act_jjyl'      : %s, """, 'int_single_list'),
        ('jjyl_time',       """ 'jjyl_time'     : %s, """, 'str'),
        ('act_zlnr',        """ 'act_zlnr'      : %s, """, 'int_single_list'),
        ('zlnr_time',       """ 'zlnr_time'     : %s, """, 'str'),
        ('act_wmzb',        """ 'act_wmzb'      : %s, """, 'int_single_list'),
        ('wmzb_time',       """ 'wmzb_time'     : %s, """, 'str'),
        ('act_sjyl',        """ 'act_sjyl'      : %s, """, 'int_single_list'),
        ('sjyl_time',       """ 'sjyl_time'     : %s, """, 'str'),
        ('act_jxdr',        """ 'act_jxdr'      : %s, """, 'int_single_list'),
        ('jxdr_time',       """ 'jxdr_time'     : %s, """, 'str'),
        ('act_zsmtx',       """ 'act_zsmtx'     : %s, """, 'int_single_list'),
        ('zsmtx_time',      """ 'zsmtx_time'    : %s, """, 'str'),
        ('act_qmzp',        """ 'act_qmzp'      : %s, """, 'int_single_list'),
        ('qmzp_time',       """ 'qmzp_time'     : %s, """, 'str'),
        ('act_czjj',        """ 'act_czjj'      : %s, """, 'int'),
        ('czjj_time',       """ 'czjj_time'     : %s, """, 'str'),
        ('act_lsjj',        """ 'act_lsjj'      : %s, """, 'int_single_list'),
        ('lsjj_time',       """ 'lsjj_time'     : %s, """, 'str'),
        ('END', """},""", 'None'),
    ], {}

def charge():
    return [
        ('buy_id', """%s: {""", 'int'),
        ('buy_id',         """ 'cfg_id'         : %s, """, 'int'),
        ('order',          """ 'order'          : %s, """, 'int'),
        ('diamond',        """ 'diamond'        : %s, """, 'int'),
        ('gift_diamond',   """ 'gift_diamond'   : %s, """, 'int'),
        ('buy_times',      """ 'buy_times'      : %s, """, 'int'),
        ('is_first',       """ 'is_first'       : %s, """, 'int'),
        ('first_diamond',  """ 'first_diamond'  : %s, """, 'int'),
        ('price',          """ 'price'          : %s, """, 'int'),
        ('name',           """ 'name'           : %s, """, 'unicode'),
        ('des',            """ 'des'            : %s, """, 'unicode'),
        ('open_gift',      """ 'open_gift'      : %s, """, 'int'),
        #('day_num',        """ 'day_num'        : %s, """, 'int'),
        ('first_gift',     """ 'first_gift'     : %s, """, 'list'),
        ('is_show',        """ 'is_show'        : %s, """, 'int'),
        ('icon',           """ 'icon'           : %s, """, 'str'),
        ('cost',           """ 'cost'           : %s, """, 'str'),
        ('sp_diamond',     """ 'sp_diamond'     : %s, """, 'int'),
        ('END', """},""", 'None'),
    ], {}

def week_gift():
    return [
        ('id', """%s: {""", 'int'),
        ('daily_gift',     """ 'daily_gift'     : %s, """, 'list'),
        ('END', """},""", 'None'),
    ], {}

def month_gift():
    return week_gift()

def user_info():
    return [
        ('level', """%s: {""", 'int'),
        ('level',         """ 'cfg_id'       : %s,""", 'int'),
        ('exp',           """ 'exp'          : %s,""", 'int'),
        ('lvexp',         """ 'lvexp'        : %s,""", 'int'),
        ('energy',        """ 'energy'       : %s,""", 'int'),
        ('energytop',     """ 'energytop'    : %s,""", 'int'),
        ('battlepoint',   """ 'battlepoint'  : %s,""", 'int'),
        ('battlepointtop',""" 'battlepointtop': %s,""", 'int'),
        ('friend_num',    """ 'friend_num'   : %s,""", 'int'),
        ('arena_exp',     """ 'arena_exp'    : %s,""", 'int'),
        ('arena_money',   """ 'arena_money'  : %s,""", 'int'),
        ('add_energy',    """ 'add_energy'   : %s,""", 'int'),
        ('add_battlepoint',""" 'add_battlepoint': %s,""", 'int'),
        ('money_sponsor', """ 'money_sponsor': %s,""", 'int'),
        ('money_rent',    """ 'money_rent'   : %s,""", 'int'),
        ('sub_num',       """ 'sub_num'      : %s,""", 'int'),
        ('rent_num',      """ 'rent_num'     : %s,""", 'int'),
        ('player_num',    """ 'player_num'   : %s,""", 'int'),
        ('equip_num',     """ 'equip_num'    : %s,""", 'int'),
        ('giveenergy',    """ 'giveenergy'   : %s,""", 'int'),
        ('givemax',       """ 'givemax'      : %s,""", 'int'),
        ('receivemax',    """ 'receivemax'   : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def user_select():
    return [
        ('id', """%s: {""", 'int'),
        ('id',            """ 'cfg_id'       : %s,""", 'int'),
        ('chenghao',      """ 'chenghao'     : %s,""", 'unicode'),
        ('index_ids',     """ 'index_ids'    : %s,""", 'int'),
        ('pos',           """ 'pos'          : %s,""", 'int'),
        ('name',          """ 'name'         : %s,""", 'str'),
        ('name_des',      """ 'name_des'     : %s,""", 'unicode'),
        ('name_des2',     """ 'name_des2'    : %s,""", 'unicode'),
        ('name_des2card', """ 'name_des2card': %s,""", 'str'),
        ('icon',          """ 'icon'         : %s,""", 'str'),
        ('name_des3',     """ 'name_des3'    : %s,""", 'unicode'),
        ('name_des3card', """ 'name_des3card': %s,""", 'str'),
        ('player_lv5',    """ 'player_lv5'   : %s,""", 'int'),
        ('story',         """ 'story'        : %s,""", 'unicode'),
        ('strategy',      """ 'strategy'     : %s,""", 'int'),
        ('',              """ 'pg'           : [""", 'None'),
        ('pg1',           """                   %s,""", 'int'),
        ('pg2',           """                   %s,""", 'int'),
        ('pg3',           """                   %s,""", 'int'),
        ('',              """                  ],""", 'None'),
        ('',              """ 'sg'           : [""", 'None'),
        ('sg1',           """                   %s,""", 'int'),
        ('sg2',           """                   %s,""", 'int'),
        ('sg3',           """                   %s,""", 'int'),
        ('',              """                  ],""", 'None'),
        ('',              """ 'sf'           : [""", 'None'),
        ('sf1',           """                   %s,""", 'int'),
        ('sf2',           """                   %s,""", 'int'),
        ('sf3',           """                   %s,""", 'int'),
        ('',              """                  ],""", 'None'),
        ('',              """ 'pf'           : [""", 'None'),
        ('pf1',           """                   %s,""", 'int'),
        ('pf2',           """                   %s,""", 'int'),
        ('pf3',           """                   %s,""", 'int'),
        ('',              """                  ],""", 'None'),
        ('',              """ 'c'            : [""", 'None'),
        ('c1',            """                   %s,""", 'int'),
        ('c2',            """                   %s,""", 'int'),
        ('c3',            """                   %s,""", 'int'),
        ('',              """                  ],""", 'None'),
        ('',              """ 'default'      : {""", 'None'),
        ('default_pg',    """                   'pg': %s,""", 'int'),
        ('default_sg',    """                   'sg': %s,""", 'int'),
        ('default_sf',    """                   'sf': %s,""", 'int'),
        ('default_pf',    """                   'pf': %s,""", 'int'),
        ('default_c',     """                   'c': %s,""", 'int'),
        ('',              """                  },""", 'None'),
        ('',              """ 'player'       : [""", 'None'),
        ('player6',       """                   %s,""", 'int'),
        ('player7',       """                   %s,""", 'int'),
        ('player8',       """                   %s,""", 'int'),
        ('player9',       """                   %s,""", 'int'),
        ('player10',      """                   %s,""", 'int'),
        ('',              """                ],""", 'None'),
        ('END', """},""", 'None'),
        ], {}

def resource():
    return [
        ('resourceid',       """%s: {""", 'int'),
        ('resourceid',       """      'cfg_id'          : %s,""", 'int'),
        ('emotion_happy',    """      'emotion_happy'   : %s,""", 'str'),
        ('emotion_normal',   """      'emotion_normal'  : %s,""", 'str'),
        ('emotion_defeated', """      'emotion_defeated': %s,""", 'str'),
        ('emotion_tired',    """      'emotion_tired'   : %s,""", 'str'),
        ('hoop',             """      'hoop'            : %s,""", 'int'),
        ('head_dongzuo',     """      'head_dongzuo'    : %s,""", 'str'),
        ('body_dongzuo',     """      'body_dongzuo'    : %s,""", 'str'),
        ('END', """},""", 'None'),
        ], {}

def monster_detail():
    handle_funcs = {}
    return [
        ('id', """%s: {""", 'int'),
        ('id',               """ 'cfg_id'   : %s,""", 'int'),
        ('name',             """ 'name'     : %s,""", 'unicode'),
        ('samename',         """ 'samename' : %s,""", 'unicode'),
        ('totalrate',        """ 'totalrate': %s,""", 'int'),
        ('star',             """ 'star'     : %s,""", 'int'),
        ('maxstar',          """ 'maxstar'  : %s,""", 'int'),
        ('starplus',         """ 'starplus' : %s,""", 'int'),
        ('story',            """ 'story'    : %s,""", 'unicode'),
        ('lv',               """ 'maxlv'    : %s,""", 'int'),
        ('lv',               """ 'level'    : %s,""", 'int'),
        ('position1',        """ 'position1': %s,""", 'int'),
        ('position2',        """ 'position2': %s,""", 'int'),
        ('',                 """ 'posfit': [""", 'None'),
        ('pos1fit',          """              %s,""", 'float'),
        ('pos2fit',          """              %s,""", 'float'),
        ('pos3fit',          """              %s,""", 'float'),
        ('pos4fit',          """              %s,""", 'float'),
        ('pos5fit',          """              %s,""", 'float'),
        ('',                 """           ],""", 'None'),
        ('team',             """ 'team'     : %s,""", 'str'),
        ('',                 """ 'shoot': {""", 'None'),
        ('pt3shoot',         """             'pt3'  : %s,""", 'int'),
        ('pt2shoot',         """             'pt2'  : %s,""", 'int'),
        ('layupshoot',       """             'layup': %s,""", 'int'),
        ('',                 """          },""", 'None'),
        ('',                 """ 'weight'  : {""", 'None'),
        ('pt3weight',        """            'pt3'  : %s,""", 'float'),
        ('pt2weight',        """            'pt2'  : %s,""", 'float'),
        ('layupweight',      """            'layup': %s,""", 'float'),
        ('',                 """           },""", 'None'),
        ('specialshoot',     """ 'specialshoot'   : %s,""", 'unicode'),
        ('player_tendency',  """ 'player_tendency': %s,""", 'int'),
        ('rare_fix',         """ 'rare_fix'       : %s,""", 'int'),
        ('atk_type',         """ 'atk_type'       : %s,""", 'int'),
        ('def_type',         """ 'def_type'       : %s,""", 'int'),
        ('',                 """ 'init': {""", 'None'),
        ('ini_pt3',          """              'pt3'  : %s,""", 'int'),
        ('ini_pt2',          """              'pt2'  : %s,""", 'int'),
        ('ini_layup',        """              'layup': %s,""", 'int'),
        ('ini_steal',        """              'steal': %s,""", 'int'),
        ('ini_inter',        """              'inter': %s,""", 'int'),
        ('ini_block',        """              'block': %s,""", 'int'),
        ('ini_ctrl',         """              'ctrl' : %s,""", 'int'),
        ('ini_reb',          """              'reb'  : %s,""", 'int'),
        ('ini_will',         """              'will' : %s,""", 'int'),
        ('',                 """         },""", 'None'),
        ('skill_active',     """ 'skill_active' : %s,""", 'int'),
        ('skill_activeshow', """ 'skill_activeshow': %s,""", 'str'),
        ('',                 """ 'skill_passive' : [""", 'None'),
        ('skill_passive1',   """                     %s,""", 'int'),
        ('skill_passive2',   """                     %s,""", 'int'),
        ('skill_passive3',   """                     %s,""", 'int'),
        ('skill_passive4',   """                     %s,""", 'int'),
        ('',                 """                   ],""", 'None'),
        ('freethrow',        """ 'freethrow'       : %s,""", 'float'),
        ('resource',         """ 'resource'        : %s,""", 'int'),
        ('card_image',       """ 'card_image'      : %s,""", 'str'),
        ('border_image',     """ 'border_image'    : %s,""", 'int'),
        ('icon_image',       """ 'icon_image'      : %s,""", 'str'),
        ('counter_type',     """ 'counter_type'    : %s,""", 'int'),
        #('counter_effect',   """ 'counter_effect'  : %s,""", 'int'),
        #('equip_effect',     """ 'equip_effect'    : %s,""", 'int'),
        ('',                 """ 'from': 2,""", 'None'),
        ('END', """},""", 'None'),
        ], handle_funcs

monster_arena = monster_vs = monster_robpatch = monster_op = monster_money =\
monster_system = monster_main = monster_main11 = monster_main21 = monster_main31 =\
monster_1v1 = monster_dynasty = monster_legend = monster_detail

def player_detail():
    handle_funcs = {}
    return [
        ('player_id', """%s: {""", 'int'),
        ('player_id',        """ 'cfg_id'   : %s,""", 'int'),
        ('star',             """ 'star'     : %s,""", 'int'),
        ('starplus',         """ 'starplus' : %s,""", 'int'),
        ('maxstar',          """ 'maxstar'  : %s,""", 'int'),
        ('maxlv',            """ 'maxlv'    : %s,""", 'int'),
        ('samename',         """ 'samename' : %s,""", 'str'),
        ('story',            """ 'story'    : %s,""", 'unicode'),
        ('speak',            """ 'speak'    : %s,""", 'unicode'),
        ('position1',        """ 'position1': %s,""", 'int'),
        ('position2',        """ 'position2': %s,""", 'int'),
        ('',                 """ 'posfit': [""", 'None'),
        ('pos1fit',          """              %s,""", 'float'),
        ('pos2fit',          """              %s,""", 'float'),
        ('pos3fit',          """              %s,""", 'float'),
        ('pos4fit',          """              %s,""", 'float'),
        ('pos5fit',          """              %s,""", 'float'),
        ('',                 """           ],""", 'None'),
        ('team',             """ 'team'     : %s,""", 'int'),
        # ('salary',           """ 'salary'   : %s,""", 'int'),
        ('exp_sort',         """ 'exp_sort'     : %s,""", 'int'),
        ('material_sort',    """ 'material_sort': %s,""", 'int'),
        ('is_eaten',         """ 'is_eaten'     : %s,""", 'int'),
        ('is_sell',          """ 'is_sell'      : %s,""", 'int'),
        ('is_retire',        """ 'is_retire'    : %s,""", 'int'),
        ('is_lock',          """ 'is_lock'      : %s,""", 'int'),
        ('',                 """ 'shoot'     : {""", 'None'),
        ('pt3shoot',         """                 'pt3'  : %s,""", 'int'),
        ('pt2shoot',         """                 'pt2'  : %s,""", 'int'),
        ('layupshoot',       """                 'layup': %s,""", 'int'),
        ('',                 """               },""", 'None'),
        ('specialshoot',     """ 'specialshoot'   : %s,""", 'unicode'),
        ('mark',             """ 'mark'           : %s,""", 'int'),
        ('player_tendency',  """ 'player_tendency': %s,""", 'int'),
        ('rare_fix',         """ 'rare_fix'       : %s,""", 'int'),
        ('atk_type',         """ 'atk_type'       : %s,""", 'int'),
        ('def_type',         """ 'def_type'       : %s,""", 'int'),
        ('',                 """ 'init': {""", 'None'),
        ('ini_pt3',          """              'pt3'  : %s,""", 'float'),
        ('ini_pt2',          """              'pt2'  : %s,""", 'float'),
        ('ini_layup',        """              'layup': %s,""", 'float'),
        ('ini_steal',        """              'steal': %s,""", 'float'),
        ('ini_inter',        """              'inter': %s,""", 'float'),
        ('ini_block',        """              'block': %s,""", 'float'),
        ('ini_ctrl',         """              'ctrl' : %s,""", 'float'),
        ('ini_reb',          """              'reb'  : %s,""", 'float'),
        ('ini_will',         """              'will' : %s,""", 'float'),
        ('',                 """         },""", 'None'),
        ('',                 """ 'grow': {""", 'None'),
        ('grow_pt3',         """              'pt3'  : %s,""", 'float'),
        ('grow_pt2',         """              'pt2'  : %s,""", 'float'),
        ('grow_layup',       """              'layup': %s,""", 'float'),
        ('grow_steal',       """              'steal': %s,""", 'float'),
        ('grow_inter',       """              'inter': %s,""", 'float'),
        ('grow_block',       """              'block': %s,""", 'float'),
        ('grow_ctrl',        """              'ctrl' : %s,""", 'float'),
        ('grow_reb',         """              'reb'  : %s,""", 'float'),
        ('grow_will',        """              'will' : %s,""", 'float'),
        ('',                 """         },""", 'None'),
        ('skill_active',     """ 'skill_active'    : %s,""", 'int'),
        ('maxskill_active',  """ 'maxskill_active' : %s,""", 'int'),
        ('skill_jointly',    """ 'skill_jointly'   : %s,""", 'int_single_list'),
        ('skill_activeshow', """ 'skill_activeshow': %s,""", 'str'),
        ('',                 """ 'skill_passive' : [""", 'None'),
        ('skill_passive1',   """                     %s,""", 'int'),
        ('skill_passive2',   """                     %s,""", 'int'),
        ('skill_passive3',   """                     %s,""", 'int'),
        ('skill_passive4',   """                     %s,""", 'int'),
        ('',                 """                   ],""", 'None'),
        ('',                 """ 'skill_lock'    : [""", 'None'),
        ('skill1lock',       """                     %s,""", 'int'),
        ('skill2lock',       """                     %s,""", 'int'),
        ('skill3lock',       """                     %s,""", 'int'),
        ('skill4lock',       """                     %s,""", 'int'),
        ('',                 """                   ],""", 'None'),
        ('freethrow',        """ 'freethrow'       : %s,""", 'float'),
        ('equipid',          """ 'equipid'         : %s,""", 'int'),
        ('resource',         """ 'resource'        : %s,""", 'int'),
        ('card_image',       """ 'card_image'      : %s,""", 'str'),
        ('border_image',     """ 'border_image'    : %s,""", 'int'),
        ('icon_image',       """ 'icon_image'      : %s,""", 'str'),
        ('is_rent',          """ 'is_rent'         : %s,""", 'int'),
        ('evolution_num',    """ 'evolution_num'   : %s,""", 'int'),
        ('',                 """ 'weight'  : {""", 'None'),
        ('pt3weight',        """            'pt3'  : %s,""", 'float'),
        ('pt2weight',        """            'pt2'  : %s,""", 'float'),
        ('layupweight',      """            'layup': %s,""", 'float'),
        ('',                 """           },""", 'None'),
        ('totalrate',        """ 'totalrate': %s,""", 'int'),
        ('name',             """ 'name'     : %s,""", 'unicode'),
        ('shortname',        """ 'shortname': %s,""", 'unicode'),
        ('is_superstar',     """ 'is_superstar'    : %s,""", 'int'),
        ('starlevel',        """ 'starlevel'       : %s,""", 'int'),
        ('sameevolution',    """ 'sameevolution'   : %s,""", 'str'),
        ('maxstarlevel',     """ 'maxstarlevel'    : %s,""", 'int'),
        ('is_keep_skill',    """ 'is_keep_skill'   : %s,""", 'int'),
        ('',                 """ 'skill_text'    : [""", 'None'),
        ('skill1text',       """                     %s,""", 'unicode'),
        ('skill2text',       """                     %s,""", 'unicode'),
        ('skill3text',       """                     %s,""", 'unicode'),
        ('skill4text',       """                     %s,""", 'unicode'),
        ('',                 """                   ],""", 'None'),
        ('counter_type',     """ 'counter_type'    : %s,""", 'int'),
        ('counter_effect',   """ 'counter_effect'  : %s,""", 'int'),
        ('equip_effect',     """ 'equip_effect'    : %s,""", 'int'),
        ('player_index',     """ 'player_index'    : %s,""", 'list'),
        ('new_star',         """ 'new_star'        : %s,""", 'int'),
        ('',                 """ 'from': 1,""", 'None'),
        ('END', """},""", 'None'),
        ], handle_funcs

player_detail6a = player_detail6b = player_detail5 = player_detail4a = player_detail4b = \
player_detail3a = player_detail3b = player_detail2a = player_detail2b = \
player_detail1a = player_detail1b = player_detail1c = player_detail

def player_book():
    return [
        ('player_id', """%s: {""", 'int'),
        ('player_id', """      'cfg_id': %s,""", 'int'),
        ('order',     """      'order' : %s,""", 'int'),
        ('team',      """      'team'  : %s,""", 'int'),
        ('conf',      """      'conf'  : %s,""", 'int'),
        ('zoneid',    """      'zoneid': %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def player_exp():
    template = [('player_level', """%s: {""", 'int')]
    for i in xrange(1, 15):
        template.extend([
        ('',                     """    %s: {""" % i, 'None'),
        ('need_exp_type%s' % i , """          'need_exp'  : %s,""", 'int'),
        ('eaten_exp_type%s' % i, """          'eaten_exp' : %s,""", 'int'),
        ('sell_money%s' % i,     """          'sell_money': %s,""", 'int'),
        ('rent_money%s' % i,     """          'rent_money': %s,""", 'int'),
        ('need_money%s' % i,     """          'need_money': %s,""", 'int'),
        ('',                     """        },""", 'None'),
        ])
    template.append(('END', """},""", 'None'))
    return template, {}

def player_retire():
    return [
        ('player_star',  """%s: {""", 'int'),
        ('retire_tp',    """      'retire_tp'   : %s,""", 'int'),
        ('retire_money', """      'retire_money': %s,""", 'int'),
        ('cupnum',       """      'cupnum'      : %s,""", 'int'),
        ('',             """      'retire'      : [""", 'None'),
        ('retire1',      """                        %s,""", 'int'),
        ('retire2',      """                        %s,""", 'int'),
        ('retire3',      """                        %s,""", 'int'),
        ('retire4',      """                        %s,""", 'int'),
        ('retire5',      """                        %s,""", 'int'),
        ('retire6',      """                        %s,""", 'int'),
        ('retire7',      """                        %s,""", 'int'),
        ('retire8',      """                        %s,""", 'int'),
        ('retire9',      """                        %s,""", 'int'),
        ('retire10',     """                        %s,""", 'int'),
        ('',             """                     ],""", 'None'),
        ('END', """},""", 'None'),
        ], {}

def player_evolution_result():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',                  """  'cfg_id'               : %s,""", 'int'),
        ('player_lv',           """  'player_lv'            : %s,""", 'int'),
        ('cup_lv',              """  'cup_lv'               : %s,""", 'int'),
        ('money',               """  'money'                : %s,""", 'int'),
        ('bottomstarlevel',     """  'bottomstarlevel'      : %s,""", 'int'),
        ('topstarlevel',        """  'topstarlevel'         : %s,""", 'int'),
        ('cupnum',              """  'cupnum'               : %s,""", 'int'),
        ('cupitem',             """  'cupitem'              : %s,""", 'int'),
        ('starlevel',           """  'starlevel'            : %s,""", 'int'),
        ('playerbottom',        """  'playerbottom'         : %s,""", 'int'),
        ('playertop',           """  'playertop'            : %s,""", 'int'),
        ('cupbottom',           """  'cupbottom'            : %s,""", 'int'),
        ('cuptop',              """  'cuptop'               : %s,""", 'int'),
        ('is_self',             """  'is_self'              : %s,""", 'int'),
        ('evolution_no',        """  'evolution_no'         : %s,""", 'unicode'),
        ('evolution_yes',       """  'evolution_yes'        : %s,""", 'unicode'),
        ('tips',                """  'tips'                 : %s,""", 'unicode'),
        ('tips2',               """  'tips2'                : %s,""", 'unicode'),
        ('needlv',              """  'needlv'               : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}

def player_rebirth_exp():
    return [
        ('player_lv',  """%s: {""", 'int'),
        ('player_lv',           """  'cfg_id'               : %s,""", 'int'),
        ('award_exp',           """  'award_exp'            : %s,""", 'list'),
        ('over_exp',            """  'over_exp'             : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}

def player_rebirth_material():
    return [
        ('player_id',  """%s: {""", 'int'),
        ('award_material',      """  'award_material'   : %s,""", 'list'),
        ('diamond',             """  'diamond'          : %s,""", 'int'),
        ('rebirth_id',          """  'rebirth_id'       : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}

def player_mix():
    return [
        ('star',  """%s: {""", 'int'),
        #('star',            """  'star'            : %s,""", 'int'),
        ('player_detail',   """  'player_detail'   : %s,""", 'list'),
        ('cost',            """  'cost'            : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}

def player_mixnum():
    return [
        (('star', 'num'), """%s: %s,""", ('int', 'int')),
        ], {}

def player_sameevo():
    return [
        ('samename',  """%s: {""", 'str'),
        ('starlevel40',   """   'starlevel40'  : %s,""", 'unicode'),
        ('starlevel50',   """   'starlevel50'  : %s,""", 'unicode'),
        ('starlevel60',   """   'starlevel60'  : %s,""", 'unicode'),
        ('starlevel610',  """   'starlevel610' : %s,""", 'unicode'),
        ('starlevel620',  """   'starlevel620' : %s,""", 'unicode'),
        ('starlevel630',  """   'starlevel630' : %s,""", 'unicode'),
        ('starlevel640',  """   'starlevel640' : %s,""", 'unicode'),
        ('starlevel650',  """   'starlevel650' : %s,""", 'unicode'),
        ('starlevel660',  """   'starlevel660' : %s,""", 'unicode'),
        ('starlevel70',   """   'starlevel70'  : %s,""", 'unicode'),
        ('star_warning',  """   'star_warning' : %s,""", 'unicode'),
        ('END', """},""", 'None'),
        ], {}

def award_retire():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',           """   'cfg_id'      : %s,""", 'int'),
        ('needpoint',    """   'needpoint'   : %s,""", 'int'),
        ('image',        """   'image'       : %s,""", 'str'),
        ('award',        """   'award'       : %s,""", 'list'),
        ('END', """},""", 'None'),
        ], {}

def gameshotlevel():
    return [
        ('id', """%s: {""", 'int'),
        ('id',            """ 'cfg_id'            : %s,""", 'int'),
        ('bottom',        """ 'bottom'            : %s,""", 'float'),
        ('range',         """ 'range'             : %s,""", 'float'),
        ('pt3',           """ 'pt3'               : %s,""", 'int'),
        ('pt2',           """ 'pt2'               : %s,""", 'int'),
        ('layup',         """ 'layup'             : %s,""", 'int'),
        ('pt3text',       """ 'pt3text'           : %s,""", 'unicode'),
        ('pt2text',       """ 'pt2text'           : %s,""", 'unicode'),
        ('layuptext',     """ 'layuptext'         : %s,""", 'unicode'),
        ('END', """},""", 'None'),
        ], {}

def gameshotjudge():
    return [
        ('judgeID', """%s: {""", 'int'),
        ('judgeID',         """ 'cfg_id'         : %s,""", 'int'),
        ('name',            """ 'name'           : %s,""", 'unicode'),
        ('atk_sort',        """ 'atk_sort'       : %s,""", 'str'),
        ('comparison_sort', """ 'comparison_sort': %s,""", 'str'),
        ('judge_sort',      """ 'judge_sort'     : %s,""", 'str'),
        ('x',               """ 'x'              : %s,""", 'int'),
        ('y',               """ 'y'              : %s,""", 'int'),
        ('success',         """ 'success'        : %s,""", 'int'),
        ('maxsuccess',      """ 'maxsuccess'     : %s,""", 'int'),
        ('minsuccess',      """ 'minsuccess'     : %s,""", 'int'),
        ('atime',           """ 'atime'          : %s,""", 'float'),
        ('bplus',           """ 'bplus'          : %s,""", 'float'),
        ('cpower',          """ 'cpower'         : %s,""", 'float'),
        ('suc1',            """ 'suc1'           : %s,""", 'int'),
        ('',                """ 's1'             : {""", 'None'),
        ('s1_score',        """                      'score': %s,""", 'int'),
        ('s1_ast',          """                      'ast'  : %s,""", 'int'),
        ('s1_hot',          """                      'hot'  : %s,""", 'int'),
        ('s1_foul',         """                      'foul' : %s,""", 'int'),
        ('s1_free',         """                      'free' : %s,""", 'int'),
        ('s1_event',        """                      'event': %s,""", 'int'),
        ('s1_dunk',         """                      'dunk' : %s,""", 'int'),
        ('',                """                    },""", 'None'),
        ('suc2',            """ 'suc2'           : %s,""", 'int'),
        ('',                """ 's2'             : {""", 'None'),
        ('s2_score',        """                      'score': %s,""", 'int'),
        ('s2_ast',          """                      'ast'  : %s,""", 'int'),
        ('s2_hot',          """                      'hot'  : %s,""", 'int'),
        ('s2_foul',         """                      'foul' : %s,""", 'int'),
        ('s2_free',         """                      'free' : %s,""", 'int'),
        ('s2_event',        """                      'event': %s,""", 'int'),
        ('s2_dunk',         """                      'dunk' : %s,""", 'int'),
        ('',                """                    },""", 'None'),
        ('fail1',           """ 'fail1'          : %s,""", 'int'),
        ('',                """ 'f1'             : {""", 'None'),
        ('f1_score',        """                      'score' : %s,""", 'int'),
        ('f1_steal',        """                      'steal' : %s,""", 'int'),
        ('f1_block',        """                      'block' : %s,""", 'int'),
        ('f1_hot',          """                      'hot'   : %s,""", 'int'),
        ('f1_foul',         """                      'foul'  : %s,""", 'int'),
        ('f1_extra',        """                      'extra' : %s,""", 'int'),
        ('f1_atkreb',       """                      'atkreb': %s,""", 'int'),
        ('f1_defreb',       """                      'defreb': %s,""", 'int'),
        ('f1_free',         """                      'free'  : %s,""", 'int'),
        ('f1_event',        """                      'event' : %s,""", 'int'),
        ('',                """                    },""", 'None'),
        ('fail2',           """ 'fail2'          : %s,""", 'int'),
        ('',                """ 'f2'             : {""", 'None'),
        ('f2_score',        """                      'score' : %s,""", 'int'),
        ('f2_steal',        """                      'steal' : %s,""", 'int'),
        ('f2_block',        """                      'block' : %s,""", 'int'),
        ('f2_hot',          """                      'hot'   : %s,""", 'int'),
        ('f2_foul',         """                      'foul'  : %s,""", 'int'),
        ('f1_extra',        """                      'extra' : %s,""", 'int'),
        ('f1_atkreb',       """                      'atkreb': %s,""", 'int'),
        ('f2_defreb',       """                      'defreb': %s,""", 'int'),
        ('f2_free',         """                      'free'  : %s,""", 'int'),
        ('f2_event',        """                      'event' : %s,""", 'int'),
        ('',                """                    },""", 'None'),
        ('atkhot',          """ 'atkhot'         : %s,""", 'int'),
        ('defhot',          """ 'defhot'         : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def gameastcount():
    return [
        ('pos_id', """%s: {""", 'int'),
        ('pos_id',         """ 'cfg_id'       : %s,""", 'int'),
        ('ast',            """ 'ast'          : %s,""", 'int'),
        ('reb',            """ 'reb'          : %s,""", 'int'),
        ('ast_time',       """ 'ast_time'     : %s,""", 'int'),
        ('reb_time',       """ 'reb_time'     : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def gameshotcount():
    return [
        ('shots', """%s: {""", 'int'),
        ('pt2',      """ 'pt2'    : %s,""", 'int'),
        ('pt3',      """ 'pt3'    : %s,""", 'int'),
        ('layup',    """ 'layup'  : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def gameragejudge():
    return [
        ('top',           """ 'top'          : %s,""", 'int'),
        ('rage_groundup', """ 'rage_groundup': %s,""", 'int'),
        ('rage_subup',    """ 'rage_subup'   : %s,""", 'int'),
        ('ini_core',      """ 'ini_core'     : %s,""", 'int'),
        ('ini_normal',    """ 'ini_normal'   : %s,""", 'int'),
        ('shotup',        """ 'shotup'       : %s,""", 'int'),
        ('warnrage',      """ 'warnrage'     : %s,""", 'int'),
        ('top_stamina',   """ 'top_stamina'  : %s,""", 'int'),
        ('ini_stamina',   """ 'ini_stamina'  : %s,""", 'int'),
        ], {}

def gamestamina_new():
    return [
        ('rangeID', """%s: {""", 'int'),
        ('rangeID',            """ 'cfg_id'            : %s,""", 'int'),
        ('bottom',             """ 'bottom'            : %s,""", 'int'),
        ('top',                """ 'top'               : %s,""", 'int'),
        ('buff_image',         """ 'buff_image'        : %s,""", 'str'),
        ('effect',             """ 'effect'            : %s,""", 'float'),
        ('stamina_warn',       """ 'stamina_warn'      : %s,""", 'int'),
        ('stamina_subup',      """ 'stamina_subup'     : %s,""", 'int'),
        ('stamina_grounddown', """ 'stamina_grounddown': %s,""", 'int'),
        ('pt3',                """ 'pt3'               : %s,""", 'int'),
        ('pt2',                """ 'pt2'               : %s,""", 'int'),
        ('layup',              """ 'layup'             : %s,""", 'int'),
        ('steal',              """ 'steal'             : %s,""", 'int'),
        ('inter',              """ 'inter'             : %s,""", 'int'),
        ('block',              """ 'block'             : %s,""", 'int'),
        ('safestamina',        """ 'safestamina'       : %s,""", 'int'),
        ('dynasty_subup',      """ 'dynasty_subup'     : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def gamestamina_strike():
    return [
        ('a3',          """ 'a3'        : %s,""", 'float'),
        ('power3',      """ 'power3'    : %s,""", 'int'),
        ('a2',          """ 'a2'        : %s,""", 'float'),
        ('power2',      """ 'power2'    : %s,""", 'int'),
        ('a1',          """ 'a1'        : %s,""", 'float'),
        ('power1',      """ 'power1'    : %s,""", 'int'),
        ('b',           """ 'b'         : %s,""", 'float'),
        ('maxstrike',   """ 'maxstrike' : %s,""", 'int'),
        ], {}

def gamedefence():
    return [
        (('posdef', 'pos1', 'pos2', 'pos3', 'pos4', 'pos5'),
         """%s: (%s, %s, %s, %s, %s),""",
         ('int', 'int', 'int', 'int', 'int', 'int')),
        ], {}

def gameeventlibrary():
    return [
        ('eventID', """%s: {""", 'int'),
        ('eventID',         """ 'cfg_id' : %s,""", 'int'),
        ('',                """ 'default': [""", 'None'),
        ('default_text1',   """              %s,""", 'unicode'),
        ('default_text2',   """              %s,""", 'unicode'),
        ('default_text3',   """              %s,""", 'unicode'),
        ('default_text4',   """              %s,""", 'unicode'),
        ('',                """            ],""", 'None'),
        ('',                """ 'trigger1': {""", 'None'),
        ('trigger1_sort',   """              'sort': %s,""", 'int'),
        ('trigger1_value1', """              'value1': %s,""", 'int_single_list'),
        ('',                """             },""", 'None'),
        ('',                """ 'trigger1_text': [""", 'None'),
        ('trigger1_text1',  """                    %s,""", 'unicode'),
        ('trigger1_text2',  """                    %s,""", 'unicode'),
        ('trigger1_text3',  """                    %s,""", 'unicode'),
        ('trigger1_text4',  """                    %s,""", 'unicode'),
        ('',                """                  ],""", 'None'),
        ('',                """ 'trigger2': {""", 'None'),
        ('trigger2_sort',   """              'sort': %s,""", 'int'),
        ('trigger2_value1', """              'value1': %s,""", 'int_single_list'),
        ('',                """             },""", 'None'),
        ('',                """ 'trigger2_text': [""", 'None'),
        ('trigger2_text1',  """                    %s,""", 'unicode'),
        ('trigger2_text2',  """                    %s,""", 'unicode'),
        ('trigger2_text3',  """                    %s,""", 'unicode'),
        ('trigger2_text4',  """                    %s,""", 'unicode'),
        ('',                """                  ],""", 'None'),
        ('',                """ 'sound': [""", 'None'),
        ('sound1',  """                    %s,""", 'str'),
        ('sound2',  """                    %s,""", 'str'),
        ('sound3',  """                    %s,""", 'str'),
        ('sound4',  """                    %s,""", 'str'),
        ('sound5',  """                    %s,""", 'str'),
        ('sound6',  """                    %s,""", 'str'),
        ('sound7',  """                    %s,""", 'str'),
        ('sound8',  """                    %s,""", 'str'),
        ('',                """          ],""", 'None'),

        ('END', """},""", 'None'),
        ], {}

def gametime_new():
    handle_funcs = {}
    handle_funcs['rotationround1'] = lambda v: v['rotationround1']
    handle_funcs['rotationround2'] = lambda v: v['rotationround2']
    handle_funcs['rotationround3'] = lambda v: v['rotationround3']
    handle_funcs['rotationround4'] = lambda v: v['rotationround4']
    handle_funcs['rotationround5'] = lambda v: v['rotationround5']

    return [
        ('roundtime',  """ 'roundtime' : %s,""", 'int'),
        ('',           """ 'subround'  : {""", 'None'),
        ('subround1',  """                 1: %s,""", 'int'),
        ('subround2',  """                 2: %s,""", 'int'),
        ('subround3',  """                 3: %s,""", 'int'),
        ('subround4',  """                 4: %s,""", 'int'),
        ('',           """               },""", 'None'),
        ('maxstamina', """ 'maxstamina': %s,""", 'int'),
        ('maxhot',     """ 'maxhot'    : %s,""", 'int'),
        ('skipbattle', """ 'skipbattle': %s,""", 'int'),
        ('subround1_text', """ 'subround1_text': %s,""", 'unicode'),
        ('subround2_text', """ 'subround2_text': %s,""", 'unicode'),
        ('subround3_text', """ 'subround3_text': %s,""", 'unicode'),
        ('subround4_text', """ 'subround4_text': %s,""", 'unicode'),
        ('',               """ 'rotationround' : [""", 'None'),
        ('rotationround1', """                    %s,""", 'int'),
        ('rotationround2', """                    %s,""", 'int'),
        ('rotationround3', """                    %s,""", 'int'),
        ('rotationround4', """                    %s,""", 'int'),
        ('rotationround5', """                    %s,""", 'int'),
        ('',           """                      ],""", 'None'),
        ('a',             """ 'a'            : %s,""", 'float'),
        ('b',             """ 'b'            : %s,""", 'float'),
        ('c',             """ 'c'            : %s,""", 'float'),
        ('ini_grow',      """ 'ini_grow'     : %s,""", 'list'),
        ('text',          """ 'text'         : %s,""", 'list'),
        ('countdown',     """ 'countdown'    : %s,""", 'int'),
        ('is_auto',       """ 'is_auto'      : %s,""", 'int'),
        ('countdown3',    """ 'countdown3'   : %s,""", 'int'),
        ('round_max',     """ 'round_max'    : %s,""", 'int'),
        ('skillnormal',   """ 'skillnormal'  : %s,""", 'int'),
        ('skillot',       """ 'skillot'      : %s,""", 'int'),
        ], handle_funcs

def gamereporter():
    return [
        ('reporterID', """%s: {""", 'int'),
        ('reporterID',     """ 'cfg_id'        : %s,""", 'int'),
        ('trigger_sort',   """ 'trigger_sort'  : %s,""", 'int'),
        ('trigger_value1', """ 'trigger_value1': %s,""", 'str'),
        ('trigger_value2', """ 'trigger_value2': %s,""", 'str'),
        ('texttime',       """ 'texttime'      : %s,""", 'int'),
        ('eventID',        """ 'textevent'     : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def gamecounter():
    return [
        ('id', """%s: {""", 'int'),
        ('id',           """ 'cfg_id'      : %s,""", 'int'),
        ('name',         """ 'name'        : %s,""", 'unicode'),
        ('counter_id',   """ 'counter_id'  : %s,""", 'int_single_list'),
        ('effect_value', """ 'effect_value': %s,""", 'int'),
        ('image',        """ 'image'       : %s,""", 'str'),
        ('description',  """ 'description' : %s,""", 'unicode'),
        ('END', """},""", 'None'),
        ], {}

def strategy():
    return [
        ('strategyID', """%s: {""", 'int'),
        ('strategyID',     """ 'cfg_id'        : %s,""", 'int'),
        ('samestrategy',   """ 'samestrategy'  : %s,""", 'int'),
        ('star',           """ 'star'          : %s,""", 'int'),
        ('strategy_image', """ 'strategy_image': %s,""", 'str'),
        ('coach',          """ 'coach'         : %s,""", 'str'),
        ('name',           """ 'name'          : %s,""", 'unicode'),
        ('suggest_player', """ 'suggest_player': %s,""", 'int_single_list'),
        ('level',          """ 'level'         : %s,""", 'int'),
        ('need_money',     """ 'need_money'    : %s,""", 'int'),
        ('need_tp',        """ 'need_tp'       : %s,""", 'int'),
        ('core_pos',       """ 'core_pos'      : %s,""", 'int_single_list'),
        ('core_short',     """ 'core_short'    : %s,""", 'unicode'),
        ('core_text',      """ 'core_text'     : %s,""", 'unicode'),
        ('description',    """ 'description'   : %s,""", 'unicode'),
        ('tips',           """ 'tips'          : %s,""", 'unicode'),
        ('',               """ 'ability1'      : {""", 'None'),
        ('ability1',       """                     'ability': %s,""", 'int'),
        ('value_x1',       """                     'value_x': %s,""", 'int'),
        ('value_y1',       """                     'value_y': %s,""", 'int'),
        ('value_z1',       """                     'value_z': %s,""", 'int_single_list'),
        ('',               """                   },""", 'None'),
        ('',               """ 'ability2'      : {""", 'None'),
        ('ability2',       """                     'ability': %s,""", 'int'),
        ('value_x2',       """                     'value_x': %s,""", 'int'),
        ('value_y2',       """                     'value_y': %s,""", 'int'),
        ('value_z2',       """                     'value_z': %s,""", 'int_single_list'),
        ('',               """                   },""", 'None'),
        ('unlockuserlv',   """ 'unlockuserlv'  : %s,""", 'int'),
        ('unlockvip',      """ 'unlockvip'     : %s,""", 'int'),
        ('',               """ 'default'       : [""", 'None'),
        ('pos1',           """                    %s,""", 'int'),
        ('pos2',           """                    %s,""", 'int'),
        ('pos3',           """                    %s,""", 'int'),
        ('pos4',           """                    %s,""", 'int'),
        ('pos5',           """                    %s,""", 'int'),
        ('pos6',           """                    %s,""", 'int'),
        ('pos7',           """                    %s,""", 'int'),
        ('pos8',           """                    %s,""", 'int'),
        ('pos9',           """                    %s,""", 'int'),
        ('pos10',          """                    %s,""", 'int'),
        ('',               """                  ],""", 'None'),
        ('counter_show',   """ 'counter_show'  : %s,""", 'int'),
        ('reset_cost',     """ 'reset_cost'    : %s,""", 'int'),
        ('need_pvestar',   """ 'need_pvestar'  : %s,""", 'int'),
        ('emblem',         """ 'emblem'        : %s,""", 'list'),
        ('END', """},""", 'None'),
        ], {}

def skill_active():
    return [
        ('skill_activeid', """%s: {""", 'int'),
        ('skill_activeid', """ 'cfg_id'       : %s,""", 'int'),
        ('sameskill',      """ 'sameskill'    : %s,""", 'int'),
        ('anime',          """ 'anime'        : %s,""", 'int'),
        ('name',           """ 'name'         : %s,""", 'unicode'),
        ('image',          """ 'image'        : %s,""", 'str'),
        ('description',    """ 'description'  : %s,""", 'unicode'),
        ('skilltip',       """ 'skilltip'     : %s,""", 'unicode'),
        ('speak',          """ 'speak'        : %s,""", 'unicode'),
        ('level',          """ 'level'        : %s,""", 'int'),
        ('exp',            """ 'need_exp'     : %s,""", 'int'),
        ('add_exp',        """ 'add_exp'      : %s,""", 'int'),
        ('need_rage',      """ 'need_rage'    : %s,""", 'int'),
        ('last_cd',        """ 'last_cd'      : %s,""", 'int'),
        ('effect_sort',    """ 'effect_sort'  : %s,""", 'int'),
        ('effect_value1',  """ 'value1'       : %s,""", 'int_0_list'),
        ('effect_value2',  """ 'value2'       : %s,""", 'int_0_list'),
        ('effect_value3',  """ 'value3'       : %s,""", 'str_list'),
        ('effect_value4',  """ 'value4'       : %s,""", 'int_0_list'),
        ('power',          """ 'power'        : %s,""", 'int'),
        ('buff',           """ 'buff'         : %s,""", 'unicode'),
        ('casttip',        """ 'casttip'      : %s,""", 'unicode'),
        ('is_motion',      """ 'is_motion'    : %s,""", 'int'),
        ('cooldown',       """ 'cooldown'     : %s,""", 'int'),
        ('trigger_sort',   """ 'trigger_sort' : %s,""", 'int'),
        ('trigger_value',  """ 'trigger_value': %s,""", 'int'),
        ('limittime',      """ 'limittime'    : %s,""", 'list'),
        ('event',          """ 'event'        : %s,""", 'int'),
        ('is_1v1',         """ 'is_1v1'       : %s,""", 'int'),
        ('',                """ 'sound': [""", 'None'),
        ('sound1',  """                    %s,""", 'str'),
        ('sound2',  """                    %s,""", 'str'),
        ('',                """          ],""", 'None'),
        ('END', """},""", 'None'),
        ], {}

def skill_passive():
    return [
        ('skill_passiveID', """%s: {""", 'int'),
        ('skill_passiveID', """ 'cfg_id'      : %s,""", 'int'),
        ('name',            """ 'name'        : %s,""", 'unicode'),
        ('icon',            """ 'icon'        : %s,""", 'str'),
        ('detail',          """ 'detail'      : %s,""", 'unicode'),
        ('starshow',        """ 'starshow'    : %s,""", 'int'),
        ('effect_sort',     """ 'effect_sort' : %s,""", 'int'),
        ('value1',          """ 'value1'      : %s,""", 'int'),
        ('value2',          """ 'value2'      : %s,""", 'float'),
        ('is_append',       """ 'is_append'   : %s,""", 'int'),
        ('weight',          """ 'weight'      : %s,""", 'int'),
        ('lotterylevel',    """ 'lotterylevel': %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def skill_passivetrain():
    handle_funcs = {}
    handle_funcs['lock1'] = lambda v: v['lock1']
    handle_funcs['lock2'] = lambda v: v['lock2']
    handle_funcs['lock3'] = lambda v: v['lock3']

    return [
        ('traintime', """%s: {""", 'int'),
        ('training_point', """ 'training_point': %s,""", 'int'),
        ('diamond',        """ 'diamond'       : %s,""", 'int'),
        ('',               """ 'lock'          : [""", 'None'),
        ('lock1',          """                     %s,""", 'float'),
        ('lock2',          """                     %s,""", 'float'),
        ('lock3',          """                     %s,""", 'float'),
        ('',               """                   ],""", 'None'),
        ('',               """ 'introtext'     : [""", 'None'),
        ('introtext1',     """                     %s,""", 'unicode'),
        ('introtext2',     """                     %s,""", 'unicode'),
        ('introtext3',     """                     %s,""", 'unicode'),
        ('introtext4',     """                     %s,""", 'unicode'),
        ('introtext5',     """                     %s,""", 'unicode'),
        ('',               """                   ],""", 'None'),
        ('superrange',     """ 'superrange'    : %s,""", 'list'),
        ('supertext',      """ 'supertext'     : %s,""", 'unicode'),
        ('goodrange',      """ 'goodrange'     : %s,""", 'list'),
        ('goodtext',       """ 'goodtext'      : %s,""", 'unicode'),
        ('normalrange',    """ 'normalrange'   : %s,""", 'list'),
        ('normaltext',     """ 'normaltext'    : %s,""", 'unicode'),
        ('badrange',       """ 'badrange'      : %s,""", 'list'),
        ('badtext',        """ 'badtext'       : %s,""", 'unicode'),
        ('END', """},""", 'None'),
        ], handle_funcs

def skill_jointly():
    handle_funcs = {}
    handle_funcs['jointly_player1'] = lambda v: v['jointly_player1']
    handle_funcs['jointly_player2'] = lambda v: v['jointly_player2']
    handle_funcs['jointly_player3'] = lambda v: v['jointly_player3']
    handle_funcs['jointly_player4'] = lambda v: v['jointly_player4']
    handle_funcs['jointly_player5'] = lambda v: v['jointly_player5']

    return [
        ('id', """%s: {""", 'int'),
        ('id',              """ 'cfg_id'        : %s,""", 'int'),
        ('name',            """ 'name'          : %s,""", 'unicode'),
        ('description',     """ 'description'   : %s,""", 'unicode'),
        ('jointly_team',    """ 'jointly_team'  : %s,""", 'int'),
        ('jointly_equip',   """ 'jointly_equip' : %s,""", 'int_single_list'),
        ('',                """ 'jointly_player': [""", 'None'),
        ('jointly_player1', """                     %s,""", 'int_single_list'),
        ('jointly_player2', """                     %s,""", 'int_single_list'),
        ('jointly_player3', """                     %s,""", 'int_single_list'),
        ('jointly_player4', """                     %s,""", 'int_single_list'),
        ('jointly_player5', """                     %s,""", 'int_single_list'),
        ('',                """                ],""", 'None'),
        ('',                """ 'effect1'       : {""", 'None'),
        ('effect_sort1',    """                     'sort'  : %s,""", 'int'),
        ('effect_sort1_x',  """                     'sort_x': %s,""", 'int'),
        ('effect_sort1_y',  """                     'sort_y': %s,""", 'int'),
        ('',                """                   },""", 'None'),
        ('',                """ 'effect2'       : {""", 'None'),
        ('effect_sort2',    """                     'sort'  : %s,""", 'int'),
        ('effect_sort2_x',  """                     'sort_x': %s,""", 'int'),
        ('effect_sort2_y',  """                     'sort_y': %s,""", 'int'),
        ('',                """                   },""", 'None'),
        ('',                """ 'effect3'       : {""", 'None'),
        ('effect_sort3',    """                     'sort'  : %s,""", 'int'),
        ('effect_sort3_x',  """                     'sort_x': %s,""", 'int'),
        ('effect_sort3_y',  """                     'sort_y': %s,""", 'int'),
        ('',                """                   },""", 'None'),
        ('pvp_sort',        """ 'pvp_sort'      : %s,""", 'int'),
        ('type_show',       """ 'type_show'     : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], handle_funcs

def pve_chapter():
    return [
        ('chapter_ID', """%s: {""", 'int'),
        ('chapter_ID',        """ 'cfg_id'       : %s,""", 'int'),
        ('chapter_order',     """ 'chapter_order': %s,""", 'int'),
        ('chapter_name',      """ 'chapter_name' : %s,""", 'unicode'),
        ('bonus',             """ 'bonus'        : %s,""", 'int'),
        ('bonusname',         """ 'bonusname'    : %s,""", 'unicode'),
        ('bonusnum',          """ 'bonusnum'     : %s,""", 'list'),
        ('',                  """ 'bonusreward'  : [""", 'None'),
        ('bonusreward1',      """                    %s,""", 'list'),
        ('bonusreward2',      """                    %s,""", 'list'),
        ('bonusreward3',      """                    %s,""", 'list'),
        ('bonusreward4',      """                    %s,""", 'list'),
        ('',                  """                  ],""", 'None'),
        ('chapter_level',     """ 'chapter_level': %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def pve_stage():
    return [
        ('stage_ID', """%s: {""", 'int'),
        ('stage_ID',          """ 'cfg_id'           : %s,""", 'int'),
        ('chapter_ID',        """ 'chapter_ID'       : %s,""", 'int'),
        ('chapter_name',      """ 'chapter_name'     : %s,""", 'unicode'),
        ('stage_order',       """ 'stage_order'      : %s,""", 'int'),
        ('is_win',            """ 'is_win'           : %s,""", 'int'),
        ('energycost',        """ 'energycost'       : %s,""", 'int'),
        ('battlepointcost',   """ 'battlepointcost'  : %s,""", 'int'),
        ('openstages',        """ 'openstages'       : %s,""", 'int_single_list'),
        ('stage_name',        """ 'stage_name'       : %s,""", 'unicode'),
        ('stage_description', """ 'stage_description': %s,""", 'unicode'),
        ('certainloot',       """ 'certainloot'      : %s,""", 'int'),
        ('certain_value',     """ 'certain_value'    : %s,""", 'unicode'),
        ('stage_dailylimit',  """ 'stage_dailylimit' : %s,""", 'int'),
        ('stage_lootshow',    """ 'stage_lootshow'   : %s,""", 'list'),
        ('firstlootshow',     """ 'firstlootshow'    : %s,""", 'list'),
        ('level',             """ 'level'            : %s,""", 'int'),
        ('stage_sort',        """ 'stage_sort'       : %s,""", 'int'),
        ('stage_image',       """ 'stage_image'      : %s,""", 'str'),
        ('stage_border',      """ 'stage_border'     : %s,""", 'str'),
        ('stage_team',        """ 'stage_team'       : %s,""", 'str'),
        ('bgm',               """ 'bgm'              : %s,""", 'str'),
        ('city',              """ 'city'             : %s,""", 'int'),
        ('is_boss',           """ 'is_boss'          : %s,""", 'str'),
        ('energy_cost1',      """ 'energy_cost1'     : %s,""", 'int'),
        ('energy_cost2',      """ 'energy_cost2'     : %s,""", 'int'),
        ('stage_reset',       """ 'stage_reset'      : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def pve_blockdetail():
    return [
        ('block_ID', """%s: {""", 'int'),
        ('block_ID',          """ 'cfg_id'         : %s,""", 'int'),
        ('stage_ID',          """ 'stage_ID'       : %s,""", 'int'),
        ('stage_name',        """ 'stage_name'     : %s,""", 'unicode'),
        ('block_order',       """ 'block_order'    : %s,""", 'int'),
        ('block_sort',        """ 'block_sort'     : %s,""", 'int'),
        ('block_value1',      """ 'block_value1'   : %s,""", 'int'),
        ('block_value2',      """ 'block_value2'   : %s,""", 'int'),
        ('block_value3',      """ 'block_value3'   : %s,""", 'int'),
        ('block_name',        """ 'block_name'     : %s,""", 'unicode'),
        #('energycost',        """ 'energycost'     : %s,""", 'int'),
        ('is_getdiamond',     """ 'is_getdiamond'  : %s,""", 'int'),
        ('block_image',       """ 'block_image'    : %s,""", 'str'),
        ('block_front',       """ 'block_front'    : %s,""", 'str'),
        ('block_top',         """ 'block_top'      : %s,""", 'str'),
        ('block_resource',    """ 'block_resource' : %s,""", 'int_single_list'),
        ('block_scale',       """ 'block_scale'    : %s,""", 'int'),
        ('block_result',      """ 'block_result'   : %s,""", 'unicode'),
        ('block_result1st',   """ 'block_result1st': %s,""", 'unicode'),
        ('block_stop',        """ 'block_stop'     : %s,""", 'int'),
        ('block_stop1st',     """ 'block_stop1st'  : %s,""", 'int'),
        ('dialogue_num',      """ 'dialogue_num'   : %s,""", 'int'),
        ('',                  """ 'dialogue1': {""", 'None'),
        ('dialogue1',         """                'dialogue': %s,""", 'list'),
        ('dialogue1_speaker', """                'speaker' : %s,""", 'unicode'),
        ('dialogue1_image',   """                'image'   : %s,""", 'str'),
        ('',                """                },""", 'None'),
        ('',                  """ 'dialogue2': {""", 'None'),
        ('dialogue2',         """                'dialogue': %s,""", 'list'),
        ('dialogue2_speaker', """                'speaker' : %s,""", 'unicode'),
        ('dialogue2_image',   """                'image'   : %s,""", 'str'),
        ('',                """                },""", 'None'),
        ('',                  """ 'dialogue3': {""", 'None'),
        ('dialogue3',         """                'dialogue': %s,""", 'list'),
        ('dialogue3_speaker', """                'speaker' : %s,""", 'unicode'),
        ('dialogue3_image',   """                'image'   : %s,""", 'str'),
        ('',                """                },""", 'None'),
        ('',                  """ 'dialogue4': {""", 'None'),
        ('dialogue4',         """                'dialogue': %s,""", 'list'),
        ('dialogue4_speaker', """                'speaker' : %s,""", 'unicode'),
        ('dialogue4_image',   """                'image'   : %s,""", 'str'),
        ('',                """                },""", 'None'),
        ('',                  """ 'dialogue5': {""", 'None'),
        ('dialogue5',         """                'dialogue': %s,""", 'list'),
        ('dialogue5_speaker', """                'speaker' : %s,""", 'unicode'),
        ('dialogue5_image',   """                'image'   : %s,""", 'str'),
        ('',                """                },""", 'None'),
        ('END', """},""", 'None'),
        ], {}

pve_blockdetail1 = pve_blockdetail2 = pve_blockdetail3 = \
    pve_blockdetail4 = pve_blockdetail5 = pve_blockdetail6 = pve_blockdetail

def pve_gamedetail():
    return [
        ('game_id', """%s: {""", 'int'),
        ('game_id',      """ 'cfg_id'      : %s,""", 'int'),
        ('opponent_name',""" 'opponent_name': %s,""", 'unicode'),
        ('level',        """ 'level'       : %s,""", 'int'),
        ('battlegroup',  """ 'battlegroup' : %s,""", 'list'),
        ('is_guiding',   """ 'is_guiding'  : %s,""", 'int'),
        ('is_skip',      """ 'is_skip'     : %s,""", 'int'),
        ('team_ability', """ 'team_ability': %s,""", 'int'),
        ('game_section', """ 'game_section': %s,""", 'int'),
        ('strategy',     """ 'strategy'    : %s,""", 'int'),
        ('is_ot',        """ 'is_ot'       : %s,""", 'int'),
        ('is_pass',      """ 'is_pass'     : %s,""", 'int'),
        ('logo',         """ 'logo'        : %s,""", 'int'),
        ('floorid',      """ 'floorid'     : %s,""", 'int'),
        ('rankingteam',  """ 'rankingteam' : %s,""", 'int'),
        ('failplus',     """ 'failplus'    : %s,""", 'int'),
        ('',             """ 'player': [""", 'None'),
        ('player1',      """              %s,""", 'int'),
        ('player2',      """              %s,""", 'int'),
        ('player3',      """              %s,""", 'int'),
        ('player4',      """              %s,""", 'int'),
        ('player5',      """              %s,""", 'int'),
        ('player6',      """              %s,""", 'int'),
        ('player7',      """              %s,""", 'int'),
        ('player8',      """              %s,""", 'int'),
        ('player9',      """              %s,""", 'int'),
        ('player10',     """              %s,""", 'int'),
        #('player11',     """              %s,""", 'int'),
        ('',             """            ],""", 'None'),
        ('explv',        """ 'explv'       : %s,""", 'float'),
        ('expbase',      """ 'expbase'     : %s,""", 'int'),
        ('star1_range',  """ 'star1_range' : %s,""", 'int_single_list'),
        ('star1_loot',   """ 'star1_loot'  : %s,""", 'int'),
        ('star2_range',  """ 'star2_range' : %s,""", 'int_single_list'),
        ('star2_loot',   """ 'star2_loot'  : %s,""", 'int'),
        ('star3_range',  """ 'star3_range' : %s,""", 'int_single_list'),
        ('star3_loot',   """ 'star3_loot'  : %s,""", 'int'),
        ('lootnormal',   """ 'lootnormal'  : %s,""", 'int'),
        ('lootfirst',    """ 'lootfirst'   : %s,""", 'int'),
        ('energy_begin', """ 'energy_begin' : %s,""", 'int'),
        ('energy_result',""" 'energy_result': %s,""", 'int'),
        ('superskill',   """ 'superskill'   : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def pve_friendbuff():
    return [
        ('friend_num', """%s: {""", 'int'),
        ('friend_num',  """ 'cfg_id'   : %s,""", 'int'),
        ('',            """ 'buff_list': [""", 'None'),
        ('',            """               [""", 'None'),
        ('buff1effect', """                %s,""", 'int'),
        ('buff1value',  """                %s,""", 'int'),
        ('buff1weight', """                %s,""", 'int'),
        ('',            """               ],""", 'None'),
        ('',            """               [""", 'None'),
        ('buff2effect', """                %s,""", 'int'),
        ('buff2value',  """                %s,""", 'int'),
        ('buff2weight', """                %s,""", 'int'),
        ('',            """               ],""", 'None'),
        ('',            """               [""", 'None'),
        ('buff3effect', """                %s,""", 'int'),
        ('buff3value',  """                %s,""", 'int'),
        ('buff3weight', """                %s,""", 'int'),
        ('',            """               ],""", 'None'),
        ('',            """              ],""", 'None'),
        ('extrabuff',   """ 'extrabuff': %s,""", 'int'),
        ('',            """ 'maxbuffs': {""", 'None'),
        ('maxbuff1',    """               1: %s,""", 'int'),
        ('maxbuff2',    """               2: %s,""", 'int'),
        ('maxbuff3',    """               3: %s,""", 'int'),
        ('',                """         },""", 'None'),
        ('END', """},""", 'None'),
        ], {}

def pve_game1v1():
    return [
        ('game1v1_id', """%s: {""", 'int'),
        ('game1v1_id',          """ 'cfg_id'          : %s,""", 'int'),
        ('game1v1_description', """ 'game1v1_description': %s,""", 'unicode'),
        ('monsterid',           """ 'monsterid'       : %s,""", 'int'),
        ('is_pass',             """ 'is_pass'         : %s,""", 'int'),
        ('playerpos',           """ 'playerpos'       : %s,""", 'int_single_list'),
        ('gametime',            """ 'gametime'        : %s,""", 'int'),
        ('explv',               """ 'explv'           : %s,""", 'float'),
        ('expbase',             """ 'expbase'         : %s,""", 'int'),
        ('star1_range',         """ 'star1_range'     : %s,""", 'int_single_list'),
        ('star1_loot',          """ 'star1_loot'      : %s,""", 'int'),
        ('star2_range',         """ 'star2_range'     : %s,""", 'int_single_list'),
        ('star2_loot',          """ 'star2_loot'      : %s,""", 'int'),
        ('star3_range',         """ 'star3_range'     : %s,""", 'int_single_list'),
        ('star3_loot',          """ 'star3_loot'      : %s,""", 'int'),
        ('card_image',          """ 'card_image'      : %s,""", 'str'),
        ('border_image',        """ 'border_image'    : %s,""", 'str'),
        ('icon_image',          """ 'icon_image'      : %s,""", 'str'),
        ('lootnormal',          """ 'lootnormal'      : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def pve_ranking():
    return [
        ('npcid', """%s: {""", 'int'),
        ('npcid',       """ 'cfg_id'     : %s,""", 'int'),
        ('name',        """ 'name'       : %s,""", 'unicode'),
        ('description', """ 'description': %s,""", 'unicode'),
        ('',            """ 'ini_day'    : [""", 'None'),
        ('ini_day1',    """                  %s,""", 'int'),
        ('ini_day2',    """                  %s,""", 'int'),
        ('ini_day3',    """                  %s,""", 'int'),
        ('ini_day4',    """                  %s,""", 'int'),
        ('ini_day5',    """                  %s,""", 'int'),
        ('ini_day6',    """                  %s,""", 'int'),
        ('ini_day7',    """                  %s,""", 'int'),
        ('',            """                ],""", 'None'),
        ('failmax',     """ 'failmax'    : %s,""", 'int'),
        ('',            """ 'win_weight' : [""", 'None'),
        ('win0',        """                  (0, %d),""", 'int'),
        ('win1',        """                  (1, %d),""", 'int'),
        ('win2',        """                  (2, %d),""", 'int'),
        ('',            """                ],""", 'None'),
        ('conf',        """ 'conf'       : %s,""", 'int'),
        ('logo',        """ 'logo'       : %s,""", 'int'),
        ('specialpick', """ 'specialpick': %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def pvp_gamearena():
    return [
        ('npc_id', """%s: {""", 'int'),
        ('npc_id',       """ 'cfg_id'    : %s,""", 'int'),
        ('name',         """ 'name'      : %s,""", 'unicode'),
        ('lv',           """ 'lv'        : %s,""", 'int'),
        ('team_ability', """ 'team_ability': %s,""", 'int'),
        ('logo',         """ 'logo'      : %s,""", 'int'),
        ('ranktop',      """ 'ranktop'   : %s,""", 'int'),
        ('rankbottom',   """ 'rankbottom': %s,""", 'int'),
        ('strategy',     """ 'strategy'  : %s,""", 'int'),
        ('',             """ 'player': [""", 'None'),
        ('player1',      """              %s,""", 'int'),
        ('player2',      """              %s,""", 'int'),
        ('player3',      """              %s,""", 'int'),
        ('player4',      """              %s,""", 'int'),
        ('player5',      """              %s,""", 'int'),
        ('player6',      """              %s,""", 'int'),
        ('player7',      """              %s,""", 'int'),
        ('player8',      """              %s,""", 'int'),
        ('player9',      """              %s,""", 'int'),
        ('player10',     """              %s,""", 'int'),
        #('player11',     """              %s,""", 'int'),
        ('',             """            ],""", 'None'),
        ('END', """},""", 'None'),
        ], {}

def pve_dice():
    return [
        ('',             """ 'done': [""", 'None'),
        ('done1',      """              %s,""", 'int'),
        ('done2',      """              %s,""", 'int'),
        ('done3',      """              %s,""", 'int'),
        ('done4',      """              %s,""", 'int'),
        ('done5',      """              %s,""", 'int'),
        ('done6',      """              %s,""", 'int'),
        ('',             """            ],""", 'None'),
        ('',             """ 'undone': [""", 'None'),
        ('undone1',      """              %s,""", 'int'),
        ('undone2',      """              %s,""", 'int'),
        ('undone3',      """              %s,""", 'int'),
        ('undone4',      """              %s,""", 'int'),
        ('undone5',      """              %s,""", 'int'),
        ('undone6',      """              %s,""", 'int'),
        ('',             """            ],""", 'None'),
        ], {}


def pve_dicenew():
    return [
        ('id', """%s: {""", 'int'),
        ('id',         """ 'cfg_id'     : %s,""", 'int'),
        ('',        """ 'done': [""", 'None'),
        ('done1', """               %s,""", 'int'),
        ('done2', """               %s,""", 'int'),
        ('done3', """               %s,""", 'int'),
        ('done4', """               %s,""", 'int'),
        ('done5', """               %s,""", 'int'),
        ('done6', """               %s,""", 'int'),
        ('',       """   ],""", 'None'),
        ('',        """ 'undone': [""", 'None'),
        ('undone1', """             %s,""", 'int'),
        ('undone2', """             %s,""", 'int'),
        ('undone3', """             %s,""", 'int'),
        ('undone4', """             %s,""", 'int'),
        ('undone5', """             %s,""", 'int'),
        ('undone6', """             %s,""", 'int'),
        ('',       """   ],""", 'None'),
        ('stage',        """ 'stage'    : %s,""", 'list'),
        ('END', """},""", 'None'),
    ], {}


def loot():
    return [
        ('id', """%s: {""", 'int'),
        ('id',         """ 'cfg_id'     : %s,""", 'int'),
        ('loot',       """ 'loot'       : %s,""", 'list'),
        ('user_loot1', """ 'user_loot1' : %s,""", 'list'),
        ('user_loot2', """ 'user_loot2' : %s,""", 'list'),
        ('user_loot3', """ 'user_loot3' : %s,""", 'list'),
        ('user_loot4', """ 'user_loot4' : %s,""", 'list'),
        ('user_loot5', """ 'user_loot5' : %s,""", 'list'),
        ('END', """},""", 'None'),
    ], {}

loot1 = loot0 = loot


def loot_server():
    return [
        ('id', """%s: {""", 'int'),
        ('id',          """ 'cfg_id'        : %s,""", 'int'),
        ('object',      """ 'object'        : %s,""", 'single_list'),
        ('server_num',  """ 'server_num'    : %s,""", 'int'),
        ('user_num',    """ 'user_num'      : %s,""", 'int'),
        ('replace',     """ 'replace'       : %s,""", 'single_list'),
        ('cycle_detail',    """ 'cycle_detail'  : %s,""", 'int'),
        ('time_start',  """ 'time_start'    : %s,""", 'str'),
        ('time_end',    """ 'time_end'      : %s,""", 'str'),
        ('server_id',   """ 'server_id'     : %s,""", 'int_single_list'),
        ('is_gacha',    """ 'is_gacha'      : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}

def text():
    return [
        (('text_id', 'text'), """%s: %s,""", ('int', 'unicode')),
        ], {}

def item():
    return [
        ('id', """%s: {""", 'int'),
        ('id',           """ 'cfg_id'      : %s,""", 'int'),
        ('sort',         """ 'sort'        : %s,""", 'int'),
        ('value1',       """ 'value1'      : %s,""", 'int'),
        ('value2',       """ 'value2'      : %s,""", 'int'),
        ('value3',       """ 'value3'      : %s,""", 'int'),
        ('itemname',     """ 'itemname'    : %s,""", 'unicode'),
        ('description',  """ 'description' : %s,""", 'unicode'),
        ('sell_diamond', """ 'sell_diamond': %s,""", 'int'),
        ('image',        """ 'image'       : %s,""", 'str'),
        ('sign',         """ 'sign'        : %s,""", 'int'),
        ('star',         """ 'star'        : %s,""", 'int'),
        ('itemget',      """ 'itemget'     : %s,""", 'unicode'),
        ('item_index',   """ 'item_index'  : %s,""", 'list'),
        ('END', """},""", 'None'),
        ], {}

def logo():
    return [
        ('teamid', """%s: {""", 'int'),
        ('teamid',   """ 'cfg_id'   : %s,""", 'int'),
        ('name',     """ 'name'     : %s,""", 'unicode'),
        ('shortname',""" 'shortname': %s,""", 'unicode'),
        ('zoneid',  """ 'zoneid'    : %s,""", 'int'),
        ('zonename',""" 'zonename'  : %s,""", 'unicode'),
        ('order',   """ 'order'     : %s,""", 'int'),
        ('select',  """ 'select'    : %s,""", 'str'),
        ('png',     """ 'png'   : %s,""", 'str'),
        ('conf',    """ 'conf'  : %s,""", 'int'),
        ('color',   """ 'color' : %s,""", 'int'),
        ('',        """ 'player': [""", 'None'),
        ('player1', """             %s,""", 'int'),
        ('player2', """             %s,""", 'int'),
        ('player3', """             %s,""", 'int'),
        ('player4', """             %s,""", 'int'),
        ('player5', """             %s,""", 'int'),
        ('',       """            ],""", 'None'),
        ('END', """},""", 'None'),
        ], {}

def conf():
    return [
        ('confid', """%s: {""", 'int'),
        ('confid',     """ 'cfg_id'  : %s,""", 'int'),
        ('confname',   """ 'confname': %s,""", 'unicode'),
        ('END', """},""", 'None'),
        ], {}

def zone():
    return [
        ('zoneid', """%s: {""", 'int'),
        ('zoneid',   """ 'cfg_id'  : %s,""", 'int'),
        ('zonename', """ 'zonename': %s,""", 'unicode'),
        ('conf',     """ 'conf'    : %s,""", 'int'),
        ('confname', """ 'confname': %s,""", 'unicode'),
        ('END', """},""", 'None'),
        ], {}

def cost_diamond():
    template = [('rowid', """%s: {""", 'int')]
    for i in xrange(1, 18):
        template.extend([
        ('time%s' % i,    """    %s: %s,""" % (i, '%s'), 'int'),
        ])
    template.append(('END', """},""", 'None'))
    return template, {}

def robmoney():
    return [
        ('rangeid',     """%s: {""", 'int'),
        ('rangeid',     """ 'cfg_id'      : %s,""", 'int'),
        ('rangelvmin',  """  'rangelvmin' : %s,""", 'int'),
        ('rangelvmax',  """  'rangelvmax' : %s,""", 'int'),
        ('robpercent',  """  'robpercent' : %s,""", 'int'),
        ('robbase',     """  'robbase'    : %s,""", 'int'),
        ('robtop',      """  'robtop'     : %s,""", 'int'),
        ('losepercent', """  'losepercent': %s,""", 'int'),
        ('losebase',    """  'losebase'   : %s,""", 'int'),
        ('losetop',     """  'losetop'    : %s,""", 'int'),
        ('battlecost',  """  'battlecost' : %s,""", 'int'),
        ('winexplv',    """  'winexplv'   : %s,""", 'float'),
        ('winexpbase',  """  'winexpbase' : %s,""", 'int'),
        ('loseexplv',   """  'loseexplv'  : %s,""", 'float'),
        ('loseexpbase', """  'loseexpbase': %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def robpatch():
    return [
        ('item_ID',     """%s: {""", 'int'),
        ('item_ID',     """  'cfg_id'     : %s,""", 'int'),
        ('name',        """  'name'       : %s,""", 'unicode'),
        ('image',       """  'image'      : %s,""", 'str'),
        ('wrest_pro',   """  'wrest_pro'  : %s,""", 'int'),
        ('wrest_pro1',  """  'wrest_pro1' : %s,""", 'int'),
        ('losemoney',   """  'losemoney'  : %s,""", 'int'),
        ('battlecost',  """  'battlecost' : %s,""", 'int'),
        ('winexplv',    """  'winexplv'   : %s,""", 'float'),
        ('winexpbase',  """  'winexpbase' : %s,""", 'int'),
        ('loseexplv',   """  'loseexplv'  : %s,""", 'float'),
        ('loseexpbase', """  'loseexpbase': %s,""", 'int'),
        ('other1_award',"""  'other1_award': %s,""", 'int'),
        ('other2_award',"""  'other2_award': %s,""", 'int'),
        ('fail_award',  """  'fail_award'  : %s,""", 'int'),
        ('order',       """  'order'       : %s,""", 'int'),
        ('star',        """  'star'        : %s,""", 'int'),
        ('lastsafe',    """  'lastsafe'    : %s,""", 'int'),

        ('',                   """  'opponents': [   """, 'None'),
        ('',                   """     [             """, 'None'),
        ('',                   """        [          """, 'None'),
        (('classA1', 'numA1'), """          (%s, %s),""", ('list', 'int')),
        (('classA2', 'numA2'), """          (%s, %s),""", ('list', 'int')),
        (('classA3', 'numA3'), """          (%s, %s),""", ('list', 'int')),
        (('classA4', 'numA4'), """          (%s, %s),""", ('list', 'int')),
        ('',                   """        ],         """, 'None'),
        ('weightA',            """        %s,        """, 'int'),
        ('',                   """     ],            """, 'None'),

        ('',                   """     [             """, 'None'),
        ('',                   """        [          """, 'None'),
        (('classB1', 'numB1'), """          (%s, %s),""", ('list', 'int')),
        (('classB2', 'numB2'), """          (%s, %s),""", ('list', 'int')),
        (('classB3', 'numB3'), """          (%s, %s),""", ('list', 'int')),
        (('classB4', 'numB4'), """          (%s, %s),""", ('list', 'int')),
        ('',                   """        ],         """, 'None'),
        ('weightB',            """        %s,        """, 'int'),
        ('',                   """     ],            """, 'None'),

        ('',                   """     [             """, 'None'),
        ('',                   """        [          """, 'None'),
        (('classC1', 'numC1'), """          (%s, %s),""", ('list', 'int')),
        (('classC2', 'numC2'), """          (%s, %s),""", ('list', 'int')),
        (('classC3', 'numC3'), """          (%s, %s),""", ('list', 'int')),
        (('classC4', 'numC4'), """          (%s, %s),""", ('list', 'int')),
        ('',                   """        ],         """, 'None'),
        ('weightC',            """        %s,        """, 'int'),
        ('',                   """     ],            """, 'None'),
        ('',                   """],                 """, 'None'),
        ('patch1_deail',  """  'patch1_deail' : %s,""", 'str'),
        ('patch2_deail',  """  'patch2_deail' : %s,""", 'str'),

        # 'opponents': [
        #     [ [(a1, num1),(a2, num2),(a3, num3),(a4, num4)],  weighta],
        #     [ [(b1, num1),(b2, num2),(b3, num3),(b4, num4)],  weightb],
        #     [ [(c1, num1),(c2, num2),(c3, num3),(c4, num4)],  weightc],
        # ]
        ('END', """},""", 'None'),
        ], {}

def robplayer():
    return [
        ('rentstar',    """%s: {""", 'int'),
        ('rentstar',    """  'cfg_id'     : %s,""", 'int'),
        ('lvmulti',     """  'lvmulti'    : %s,""", 'int'),
        ('numplus',     """  'numplus'    : %s,""", 'int'),
        ('plusmax',     """  'plusmax'    : %s,""", 'int'),
        ('safetime',    """  'safetime'   : %s,""", 'int'),
        ('totaltime',   """  'totaltime'  : %s,""", 'int'),
        ('gainpercent', """  'gainpercent': %s,""", 'int'),
        ('losemoney',   """  'losemoney'  : %s,""", 'int'),
        ('battlecost',  """  'battlecost' : %s,""", 'int'),
        ('winexplv',    """  'winexplv'   : %s,""", 'float'),
        ('winexpbase',  """  'winexpbase' : %s,""", 'int'),
        ('loseexplv',   """  'loseexplv'  : %s,""", 'float'),
        ('loseexpbase', """  'loseexpbase': %s,""", 'int'),
        ('unhirebase',  """  'unhirebase' : %s,""", 'int'),
        ('unhirelv',    """  'unhirelv'   : %s,""", 'int'),
        ('unhiretime',  """  'unhiretime' : %s,""", 'int'),
        ('unhiremax',   """  'unhiremax'  : %s,""", 'int'),
        ('baseplus',    """  'baseplus'   : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def patch_merge():
    handle_funcs = {}
    handle_funcs['patch1'] = lambda v: v['patch1']
    handle_funcs['patch2'] = lambda v: v['patch2']
    handle_funcs['patch3'] = lambda v: v['patch3']
    handle_funcs['patch4'] = lambda v: v['patch4']
    handle_funcs['patch5'] = lambda v: v['patch5']
    handle_funcs['patch6'] = lambda v: v['patch6']

    return [
        ('merge_id',     """%s: {""", 'int'),
        ('merge_id',     """  'cfg_id'      : %s,""", 'int'),
        ('name',         """  'name'        : %s,""", 'unicode'),
        ('order',        """  'order'       : %s,""", 'int'),
        ('',             """  'patch'       : [""", 'None'),
        ('patch1',       """                   %s,""", 'int'),
        ('patch2',       """                   %s,""", 'int'),
        ('patch3',       """                   %s,""", 'int'),
        ('patch4',       """                   %s,""", 'int'),
        ('patch5',       """                   %s,""", 'int'),
        ('patch6',       """                   %s,""", 'int'),
        ('',             """                 ],""", 'None'),
        ('object_equip', """  'object_equip': %s,""", 'int'),
        ('merge_money',  """  'merge_money' : %s,""", 'int'),
        ('is_show',      """  'is_show'     : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], handle_funcs

def award_ranking():
    return [
        ('id', """%s: {""", 'int'),
        ('id',          """  'cfg_id'     : %s,""", 'int'),
        ('start_rank',  """  'start_rank' : %s,""", 'int'),
        ('end_rank',    """  'end_rank'   : %s,""", 'int'),
        ('per_money',   """  'per_money'  : %s,""", 'int'),
        ('per_base',    """  'per_base'   : %s,""", 'int'),
        ('round_award', """  'round_award': %s,""", 'list'),
        ('END', """},""", 'None'),
        ], {}

def celebration():
    return [
        ('celebration_ID', """%s: {""", 'int'),
        ('celebration_ID',     """  'cfg_id'            : %s,""", 'int'),
        ('is_viplook',         """  'is_viplook'        : %s,""", 'int'),
        ('sort',               """  'sort'              : %s,""", 'int'),
        ('image',              """  'image'             : %s,""", 'str'),
        ('description',        """  'description'       : %s,""", 'unicode'),
        ('description_detail', """  'description_detail': %s,""", 'unicode'),
        ('celebration_detail', """  'celebration_detail': %s,""", 'int'),
        ('cycle_detail',       """  'cycle_detail'      : %s,""", 'int'),
        ('time_start',         """  'time_start'        : %s,""", 'str'),
        ('time_end',           """  'time_end'          : %s,""", 'str'),
        ('delay',              """  'delay'             : %s,""", 'str'),
        ('award_time',         """  'award_time'        : %s,""", 'int'),
        ('Chapter_team',       """  'Chapter_team'      : %s,""", 'list'),
        ('is_push',            """  'is_push'           : %s,""", 'int'),
        ('daily_times',        """  'daily_times'       : %s,""", 'int'),
        ('limit_start',        """  'limit_start'       : %s,""", 'str'),
        ('limit_end',          """  'limit_end'         : %s,""", 'str'),
        ('information',        """  'information'       : %s,""", 'unicode'),
        ('location_icon',      """  'location_icon'     : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def activity_e():
    return [
        ('id', """%s: {""", 'int'),
        ('id',              """  'cfg_id'       : %s,""", 'int'),
        ('sort',            """  'sort'         : %s,""", 'int'),
        ('sameact',         """  'sameact'      : %s,""", 'int'),
        ('value1',          """  'value1'       : %s,""", 'int'),
        ('value2',          """  'value2'       : %s,""", 'list'),
        ('value3',          """  'value3'       : %s,""", 'str_list'),
        ('value4',          """  'value4'       : %s,""", 'int'),
        ('detail',          """  'detail'       : %s,""", 'unicode'),
        ('award_loot',      """  'award_loot'   : %s,""", 'list'),
        ('reward_num',      """  'reward_num'   : %s,""", 'int'),
        ('limit',           """  'limit'        : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def equip_detail():
    return [
        ('equip_id', """%s: {""", 'int'),
        ('equip_id',         """  'cfg_id'     : %s,""", 'int'),
        ('name',             """  'name'       : %s,""", 'unicode'),
        ('description',      """  'description': %s,""", 'unicode'),
        ('evo_tips',         """  'evo_tips'   : %s,""", 'unicode'),
        ('image',            """  'image'      : %s,""", 'str'),
        ('sort',             """  'sort'       : %s,""", 'int'),
        ('star',             """  'star'       : %s,""", 'int'),
        ('power',            """  'power'      : %s,""", 'float'),
        ('equip_type',       """  'equip_type' : %s,""", 'int'),
        ('',                 """  'ability1': {""", 'None'),
        ('ability1',         """               'ability'  : %s,""", 'int'),
        ('value_x1',         """               'value_x'  : %s,""", 'int'),
        ('value_y1',         """               'value_y'  : %s,""", 'int'),
        ('level_up1',        """               'level_up' : %s or 1,""", 'int'),
        ('level_add1',       """               'level_add': %s,""", 'float'),
        ('',                 """              },""", 'None'),
        ('',                 """  'ability2': {""", 'None'),
        ('ability2',         """               'ability'  : %s,""", 'int'),
        ('value_x2',         """               'value_x'  : %s,""", 'int'),
        ('value_y2',         """               'value_y'  : %s,""", 'int'),
        ('level_up2',        """               'level_up' : %s or 1,""", 'int'),
        ('level_add2',       """               'level_add': %s,""", 'float'),
        ('',                 """              },""", 'None'),
        ('advanced',         """  'advanced'    : %s,""", 'int'),
        ('advanced_max',     """  'advanced_max': %s,""", 'int'),
        ('ability_add',      """  'ability_add' : %s,""", 'int'),
        ('ability_sort',     """  'ability_sort' : %s,""", 'int_single_list'),
        ('ability_addx',     """  'ability_addx' : %s,""", 'int_single_list'),
        ('ability_addy',     """  'ability_addy' : %s,""", 'int_single_list'),
        ('',                 """  'desc'        : [""", 'None'),
        ('description1',     """                   %s,""", 'unicode'),
        ('description2',     """                   %s,""", 'unicode'),
        ('description3',     """                   %s,""", 'unicode'),
        ('description4',     """                   %s,""", 'unicode'),
        ('description5',     """                   %s,""", 'unicode'),
        ('description6',     """                   %s,""", 'unicode'),
        ('',                 """                 ],""", 'None'),
        ('',                 """  'unlcok'      : [""", 'None'),
        ('unlcok1',          """                   %s,""", 'int'),
        ('unlcok2',          """                   %s,""", 'int'),
        ('unlcok3',          """                   %s,""", 'int'),
        ('unlcok4',          """                   %s,""", 'int'),
        ('unlcok5',          """                   %s,""", 'int'),
        ('unlcok6',          """                   %s,""", 'int'),
        ('',                 """                 ],""", 'None'),
        ('light',            """  'light'       : %s,""", 'int'),
        ('money_cost',       """  'money_cost'  : %s,""", 'int'),
        ('money_over',       """  'money_over'  : %s,""", 'int'),
        ('sort_name',        """  'sort_name'   : %s,""", 'unicode'),
        ('is_material',      """  'is_material' : %s,""", 'int'),
        ('playerfit',        """  'playerfit'   : %s,""", 'int_single_list'),
        ('maxlv',            """  'maxlv'       : %s,""", 'int'),
        ('material',         """  'material'    : %s,""", 'list'),
        ('cupnum',           """  'cupnum'      : %s,""", 'int'),
        ('samename',         """  'samename'    : %s,""", 'str'),
        ('mix_sort',         """  'mix_sort'    : %s,""", 'int'),
        ('tiername',         """ 'tiername'     : %s,""", 'str'),
        ('equip_tier',       """ 'equip_tier'   : %s,""", 'int'),
        ('equip_index',      """ 'equip_index'  : %s,""", 'list'),
        ('is_highlevel',     """ 'is_highlevel' : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

equip_detail1 = equip_detail2 = equip_detail3 = equip_detail4 = \
equip_detail5 = equip_detail6 = equip_detail

def equip_tier():
    handle_funcs = {}
    handle_funcs['tiername1'] = lambda v: v['tiername1']
    handle_funcs['tiername2'] = lambda v: v['tiername2']
    handle_funcs['tiername3'] = lambda v: v['tiername3']
    handle_funcs['tiername4'] = lambda v: v['tiername4']

    template = [
        ('id', """%s: {""", 'int'),
        ('id',       """  'cfg_id'       :%s,""", 'int'),
        ('name',     """  'name'         :%s,""", 'unicode'),
        ('',             """  'tiername' : [""", 'None'),
        ('tiername1',    """           %s,""", 'str'),
        ('tiername2',    """           %s,""", 'str'),
        ('tiername3',    """           %s,""", 'str'),
        ('tiername4',    """           %s,""", 'str'),
        ('',                """             ],""", 'None'),
        ('',         """  'description'  : [""", 'None'),
        ('description2', """               %s,""", 'unicode'),
        ('description3', """               %s,""", 'unicode'),
        ('description4', """               %s,""", 'unicode'),
        ('description5', """               %s,""", 'unicode'),
        ('description6', """               %s,""", 'unicode'),
        ('description7', """               %s,""", 'unicode'),
        ('description8', """               %s,""", 'unicode'),
        ('description9', """               %s,""", 'unicode'),
        ('description10',"""               %s,""", 'unicode'),
        ('',             """              ],""", 'None'),
    ]
    for i in xrange(2, 11):
        template.extend([
        ('',                """ 'ability%s_1' : {""" % i, 'None'),
        ('ability%s_1' % i,      """ 'ability' : %s,""", 'int'),
        ('value_x%s_1' % i,      """ 'value_x' : %s,""", 'int'),
        ('value_y%s_1' % i,      """ 'value_y' : %s,""", 'int'),
        ('',                """                },""", 'None'),
        ('',                """ 'ability%s_2' : {""" % i, 'None'),
        ('ability%s_2' % i,      """ 'ability' : %s,""", 'int'),
        ('value_x%s_2' % i,      """ 'value_x' : %s,""", 'int'),
        ('value_y%s_2' % i,      """ 'value_y' : %s,""", 'int'),
        ('',                """                },""", 'None'),
        ])
    template.append(('END', """},""", 'None'))
    return template, handle_funcs

def equip_type():
    template = [
        ('equip_level', """%s: {""", 'int'),
        ('',               """  'critweight_lv': [""", 'None'),
        ('critweight_lv1', """                     (1, %s),""", 'int'),
        ('critweight_lv2', """                     (2, %s),""", 'int'),
        ('critweight_lv3', """                     (3, %s),""", 'int'),
        ('critweight_lv4', """                     (4, %s),""", 'int'),
        ('critweight_lv5', """                     (5, %s),""", 'int'),
        ('critweight_lv6', """                     (6, %s),""", 'int'),
        ('',               """              ],""", 'None'),
    ]
    for i in xrange(1, 12):
        template.extend([
        ('',                       """    %s: {""" % i, 'None'),
        ('need_money_type%s' % i,  """          'need_money': %s,""", 'int'),
        ('sell_money_type%s' % i,  """          'sell_money': %s,""", 'int'),
        ('',                     """        },""", 'None'),
        ])
    template.append(('END', """},""", 'None'))
    return template, {}

def equip_retire():
    return [
        ('equip_star',  """%s: {""", 'int'),
        ('equip_star',            """  'cfg_id'               : %s,""", 'int'),
        ('retire_leaguedividend', """  'retire_leaguedividend': %s,""", 'int'),
        ('retire_leagueexp',      """  'retire_leagueexp'     : %s,""", 'int'),
        ('retire_leaguetech',     """  'retire_leaguetech'    : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def equip_rebirth_material():
    return [
        ('equip_id',  """%s: {""", 'int'),
        ('equip_id',            """  'cfg_id'           : %s,""", 'int'),
        ('award_material',      """  'award_material'   : %s,""", 'list'),
        ('award_money',         """  'award_money'      : %s,""", 'int'),
        ('diamond',             """  'diamond'          : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}

def equip_mix():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',              """  'cfg_id'          : %s,""", 'int'),
        ('star',            """  'star'            : %s,""", 'int'),
        ('equip_detail',    """  'equip_detail'    : %s,""", 'list'),
        ('cost',            """  'cost'            : %s,""", 'int'),
        ('mix_sort',        """  'mix_sort'        : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}

def equip_mixnum():
    return [
        (('star', 'num'), """%s: %s,""", ('int', 'int')),
        ], {}

def floor_detail():
    return [
        ('floorid',  """%s: {""", 'int'),
        ('floorid',       """  'cfg_id'       : %s,""", 'int'),
        ('teamname',      """  'teamname'     : %s,""", 'unicode'),
        ('centername',    """  'centername'   : %s,""", 'unicode'),
        ('lineout_r',     """  'lineout_r'    : %s,""", 'int'),
        ('lineout_g',     """  'lineout_g'    : %s,""", 'int'),
        ('lineout_b',     """  'lineout_b'    : %s,""", 'int'),
        ('linein_r',      """  'linein_r'     : %s,""", 'int'),
        ('linein_g',      """  'linein_g'     : %s,""", 'int'),
        ('linein_b',      """  'linein_b'     : %s,""", 'int'),
        ('paintout_r',    """  'paintout_r'   : %s,""", 'int'),
        ('paintout_g',    """  'paintout_g'   : %s,""", 'int'),
        ('paintout_b',    """  'paintout_b'   : %s,""", 'int'),
        ('paintin_r',     """  'paintin_r'    : %s,""", 'int'),
        ('paintin_g',     """  'paintin_g'    : %s,""", 'int'),
        ('paintin_b',     """  'paintin_b'    : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def gacha():
    handle_funcs = {}
    handle_funcs[('player_detail1', 'num1')] = lambda v: v['num1']
    handle_funcs[('player_detail2', 'num2')] = lambda v: v['num2']
    handle_funcs[('player_detail3', 'num3')] = lambda v: v['num3']
    handle_funcs[('player_detail4', 'num4')] = lambda v: v['num4']

    return [
        ('gacha_sort',  """%s: {""", 'int'),
        ('gacha_sort',     """  'cfg_id'        : %s,""", 'int'),
        ('consume_sort',   """  'consume_sort'  : %s,""", 'int'),
        ('value1',         """  'value1'        : %s,""", 'int'),
        ('value2',         """  'value2'        : %s,""", 'int'),
        ('',               """  'detail': [""", 'None'),
        (('player_detail1', 'num1'), """          (%s, %s),""", ('list', 'int')),
        (('player_detail2', 'num2'), """          (%s, %s),""", ('list', 'int')),
        (('player_detail3', 'num3'), """          (%s, %s),""", ('list', 'int')),
        (('player_detail4', 'num4'), """          (%s, %s),""", ('list', 'int')),
        ('',                     """        ],""", 'None'),
        ('free_time',      """  'free_time'     : %s,""", 'int'),
        ('firstdetail',    """  'firstdetail'   : %s,""", 'list'),
        ('first_num',      """  'first_num'     : %s,""", 'int'),
        ('firstdetail2',   """  'firstdetail2'  : %s,""", 'list'),
        ('first_num2',     """  'first_num2'    : %s,""", 'int'),
        ('safe_time',      """  'safe_times'    : %s,""", 'int'),
        ('safe_detail1',   """  'safe_detail1'  : %s,""", 'list'),
        ('safe_num1',      """  'safe_num1'     : %s,""", 'int'),
        ('patch',          """  'patch'         : %s,""", 'list'),
        ('warning_num',    """  'warning_num'   : %s,""", 'int'),
        ('sp_num',         """  'sp_num'        : %s,""", 'list'),
        ('END', """},""", 'None'),
        ], handle_funcs

def gacha_equip():
    handle_funcs = {}
    handle_funcs[('equip_detail1', 'num1')] = lambda v: v['num1']
    handle_funcs[('equip_detail2', 'num2')] = lambda v: v['num2']
    handle_funcs[('equip_detail3', 'num3')] = lambda v: v['num3']

    return [
        ('gacha_sort',  """%s: {""", 'int'),
        ('gacha_sort',     """  'cfg_id'        : %s,""", 'int'),
        ('consume_sort',   """  'consume_sort'  : %s,""", 'int'),
        ('value1',         """  'value1'        : %s,""", 'int'),
        ('value2',         """  'value2'        : %s,""", 'int'),
        ('',               """  'detail': [""", 'None'),
        (('equip_detail1', 'num1'), """          (%s, %s),""", ('list', 'int')),
        (('equip_detail2', 'num2'), """          (%s, %s),""", ('list', 'int')),
        (('equip_detail3', 'num3'), """          (%s, %s),""", ('list', 'int')),
        ('',                     """        ],""", 'None'),
        ('free_time',      """  'free_time'     : %s,""", 'int'),
        ('safe_times',     """  'safe_times'    : %s,""", 'int'),
        ('safe_detail',    """  'safe_detail'   : %s,""", 'list'),
        ('safe_num',       """  'safe_num'      : %s,""", 'int'),
        ('firstdetail',    """  'firstdetail'   : %s,""", 'list'),
        ('first_num',      """  'first_num'     : %s,""", 'int'),
        ('sp_num',         """  'sp_num'        : %s,""", 'list'),
        ('END', """},""", 'None'),
        ], handle_funcs

def goods_arena():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',           """  'cfg_id'      : %s,""", 'int'),
        ('name',         """  'name'        : %s,""", 'unicode'),
        ('description',  """  'description' : %s,""", 'unicode'),
        ('goods_type',   """  'goods_type'  : %s,""", 'int'),
        ('goods_id',     """  'goods_id'    : %s,""", 'int'),
        ('goods_num',    """  'goods_num'   : %s,""", 'int'),
        ('order',        """  'order'       : %s,""", 'int'),
        ('limit_type',   """  'limit_type'  : %s,""", 'int'),
        ('limit_value1', """  'limit_value1': %s,""", 'int'),
        ('limit_value2', """  'limit_value2': %s,""", 'int'),
        ('is_open',      """  'is_open'     : %s,""", 'int'),
        ('tp_cost',      """  'tp_cost'     : %s,""", 'int'),
        ('loot',         """  'loot'        : %s,""", 'list'),
        ('END', """},""", 'None'),
        ], {}

def vip_function():
    return [
        ('Vip_level',  """%s: {""", 'int'),
        ('Vip_level',           """  'cfg_id'               : %s,""", 'int'),
        ('charge_count',        """  'charge_count'         : %s,""", 'int'),
        ('preview',             """  'preview'              : %s,""", 'unicode'),
        ('next_preview',        """  'next_preview'         : %s,""", 'unicode'),
        ('recover_energy',      """  'recover_energy'       : %s,""", 'int'),
        ('recover_battlepoint', """  'recover_battlepoint'  : %s,""", 'int'),
        ('arena_num',           """  'arena_num'            : %s,""", 'int'),
        ('arena_add',           """  'arena_add'            : %s,""", 'int'),
        ('battle_speed',        """  'battle_speed'         : %s,""", 'int'),
        ('equip_critrange',     """  'equip_critrange'      : %s,""", 'int_single_list'),
        ('money_tree_time',     """  'money_tree_time'      : %s,""", 'int'),
        ('vip_moneystage',      """  'vip_moneystage'       : %s,""", 'int'),
        ('vip_expstage',        """  'vip_expstage'         : %s,""", 'int'),
        ('vip_free',            """  'vip_free'             : %s,""", 'int'),
        ('retire_num',          """  'retire_num'           : %s,""", 'int'),
        ('aid_num',             """  'aid_num'              : %s,""", 'int'),
        ('pmax',                """  'pmax'                 : %s,""", 'int'),
        ('plocknum',            """  'plocknum'             : %s,""", 'int'),
        ('topprey',             """  'topprey'              : %s,""", 'int'),
        ('topprey_add',         """  'topprey_add'          : %s,""", 'int'),
        ('dynastytime',         """  'dynastytime'          : %s,""", 'int'),
        ('boxgold',             """  'boxgold'              : %s,""", 'int'),
        ('boxsilver',           """  'boxsilver'            : %s,""", 'int'),
        ('vs_num',              """  'vs_num'               : %s,""", 'int'),
        ('vs_add',              """  'vs_add'               : %s,""", 'int'),
        ('regular_reset',       """  'regular_reset'        : %s,""", 'int'),
        ('sweep',               """  'sweep'                : %s,""", 'int'),
        ('energy_add',          """  'energy_add'           : %s,""", 'int'),
        ('battlepoint_add',     """  'battlepoint_add'      : %s,""", 'int'),
        ('dynasty_loot1',       """  'dynasty_loot1'        : %s,""", 'int'),
        ('dynasty_loot2',       """  'dynasty_loot2'        : %s,""", 'int'),
        ('dynasty_loot3',       """  'dynasty_loot3'        : %s,""", 'int'),
        ('dynasty_lootfirst',   """  'dynasty_lootfirst'    : %s,""", 'int'),
        ('dynasty_lootnormal',  """  'dynasty_lootnormal'   : %s,""", 'int'),
        ('exp_dailytime',       """  'exp_dailytime'        : %s,""", 'int'),
        ('money_dailytime',     """  'money_dailytime'      : %s,""", 'int'),
        ('donate_num',          """  'donate_num'           : %s,""", 'int'),
        ('H_reset',             """  'H_reset'              : %s,""", 'int'),
        ('vip_treasure',        """  'vip_treasure'         : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}


def random_name():
    return [
        ('first_name',      """  'first_name'       : %s,""", 'unicode'),
        ('middle',          """  'middle'           : %s,""", 'unicode'),
        ('last_name',       """  'last_name'        : %s,""", 'unicode'),
    ], {}, 'special'


def random_namevs():
    return [
        ('first_name',      """  'first_name'       : %s,""", 'unicode'),
        ('middle',          """  'middle'           : %s,""", 'unicode'),
        ('last_name',       """  'last_name'        : %s,""", 'unicode'),
    ], {}, 'special'

def text_hexie():
    return [
        #('id',            """  'id'             : %s,""", 'int'),
        ('name',          """  'name'           : %s,""", 'unicode'),
    ], {}, 'special'

def award_arena():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',          """  'cfg_id'     : %s,""", 'int'),
        ('start_rank',  """  'start_rank' : %s,""", 'int'),
        ('end_rank',    """  'end_rank'   : %s,""", 'int'),
        ('per_tp',      """  'per_tp'     : %s,""", 'int'),
        ('per_money',   """  'per_money'  : %s,""", 'int'),
        ('round_award', """  'round_award': %s,""", 'list'),
        #('num1',        """  'num1'       : %s,""", 'int'),
        ('battlecost',  """  'battlecost' : %s,""", 'int'),
        ('winexplv',    """  'winexplv'   : %s,""", 'float'),
        ('loseexplv',   """  'loseexplv'  : %s,""", 'float'),
        ('turnloot',        """  'turnloot'     : %s,""", 'list'),
        ('turnlootshow',    """  'turnlootshow' : %s,""", 'list'),
        ('END', """},""", 'None'),
        ], {}

def bulletin():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',     """  'cfg_id': %s,""", 'int'),
        ('title',  """  'title' : %s,""", 'unicode'),
        ('text',   """  'text'  : %s,""", 'unicode'),
        ('server', """  'server': %s,""", 'int_single_list'),
        ('day1',   """  'day1'  : %s,""", 'int'),
        ('day2',   """  'day2'  : %s,""", 'int'),
        ('cycle_detail',    """  'cycle_detail' : %s,""", 'int'),
        ('time_start',      """  'time_start'   : %s,""", 'str'),
        ('time_end',        """  'time_end'     : %s,""", 'str'),
        ('END', """},""", 'None'),
        ], {}

def gonglve():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',     """  'cfg_id': %s,""", 'int'),
        ('title',  """  'title' : %s,""", 'unicode'),
        ('text',   """  'text'  : %s,""", 'unicode'),
        ('END', """},""", 'None'),
        ], {}

def treasure():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',            """  'cfg_id'       : %s,""", 'int'),
        ('name',          """  'name'         : %s,""", 'unicode'),
        ('detail',        """  'detail'       : %s,""", 'unicode'),
        ('loot',          """  'loot'         : %s,""", 'list'),
        ('image',         """  'image'        : %s,""", 'str'),
        ('star',          """  'star'         : %s,""", 'int'),
        ('signtext',      """  'signtext'     : %s,""", 'str'),
        ('END', """},""", 'None'),
        ], {}

def goods_diamond():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',           """  'cfg_id'      : %s,""", 'int'),
        ('section',      """  'section'     : %s,""", 'int'),
        ('name',         """  'name'        : %s,""", 'unicode'),
        ('description',  """  'description' : %s,""", 'unicode'),
        ('goods_type',   """  'goods_type'  : %s,""", 'int'),
        ('goods_id',     """  'goods_id'    : %s,""", 'int'),
        ('goods_num',    """  'goods_num'   : %s,""", 'int'),
        ('order',        """  'order'       : %s,""", 'int'),
        ('limit_type',   """  'limit_type'  : %s,""", 'int'),
        ('limit_value1', """  'limit_value1': %s,""", 'int'),
        ('limit_value2', """  'limit_value2': %s,""", 'int'),
        ('is_open',      """  'is_open'     : %s,""", 'int'),
        ('cost',         """  'cost'        : %s,""", 'int'),
        ('formercost',   """  'formercost'  : %s,""", 'int'),
        ('needvip',      """  'needvip'     : %s,""", 'int'),
        ('lootshow',     """  'lootshow'    : %s,""", 'list'),
        ('END', """},""", 'None'),
        ], {}

def patchplayer():
    return [
        ('patch_id',  """%s: {""", 'int'),
        ('patch_id',       """  'cfg_id'        : %s,""", 'int'),
        ('name',           """  'name'          : %s,""", 'unicode'),
        ('story',          """  'story'         : %s,""", 'unicode'),
        ('exchange_num',   """  'exchange_num'  : %s,""", 'int'),
        ('object_warrior', """  'object_warrior': %s,""", 'int'),
        ('honor_cost',     """  'honor_cost'    : %s,""", 'int'),
        ('max_universal',  """  'max_universal' : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def patchequip():
    return [
        ('patchequip_id',  """%s: {""", 'int'),
        ('patchequip_id',  """  'cfg_id'        : %s,""", 'int'),
        ('name',           """  'name'          : %s,""", 'unicode'),
        #('story',          """  'story'         : %s,""", 'unicode'),
        ('exchange_num',   """  'exchange_num'  : %s,""", 'int'),
        ('object_equip',   """  'object_equip'  : %s,""", 'int'),
        ('money_cost',     """  'money_cost'    : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def guide():
    handle_funcs = {}
    handle_funcs['arrow1_x'] = lambda v: v['arrow1_x'] is not None
    handle_funcs['arrow1_y'] = lambda v: v['arrow1_y'] is not None
    handle_funcs['arrow1_rotate'] = lambda v: v['arrow1_rotate'] is not None
    handle_funcs['arrow2_x'] = lambda v: v['arrow2_x'] is not None
    handle_funcs['arrow2_y'] = lambda v: v['arrow2_y'] is not None
    handle_funcs['arrow2_rotate'] = lambda v: v['arrow2_rotate'] is not None
    handle_funcs['shadow1_x'] = lambda v: v['shadow1_x'] is not None
    handle_funcs['shadow1_y'] = lambda v: v['shadow1_y'] is not None
    handle_funcs['shadow1_l'] = lambda v: v['shadow1_l'] is not None
    handle_funcs['shadow1_h'] = lambda v: v['shadow1_h'] is not None
    handle_funcs['shadow2_x'] = lambda v: v['shadow2_x'] is not None
    handle_funcs['shadow2_y'] = lambda v: v['shadow2_y'] is not None
    handle_funcs['shadow2_l'] = lambda v: v['shadow2_l'] is not None
    handle_funcs['shadow2_h'] = lambda v: v['shadow2_h'] is not None
    handle_funcs['shadow3_x'] = lambda v: v['shadow3_x'] is not None
    handle_funcs['shadow3_y'] = lambda v: v['shadow3_y'] is not None
    handle_funcs['shadow3_l'] = lambda v: v['shadow3_l'] is not None
    handle_funcs['shadow3_h'] = lambda v: v['shadow3_h'] is not None

    return [
        ('id',  """%s: {""", 'int'),
        ('id',          """  'cfg_id'     : %s,""", 'int'),
        ('order',       """  'order'      : %s,""", 'int'),
        ('save',        """  'save'       : %s,""", 'int'),
        ('sectiongroup',"""  'sectiongroup': %s,""", 'int'),
        ('guidegroup',  """  'guidegroup' : %s,""", 'int'),
        ('is_savepoint',"""  'is_savepoint': %s,""", 'int'),
        ('is_battle',   """  'is_battle'  : %s,""", 'int'),
        ('function',    """  'function'   : %s,""", 'int'),
        #('interface',   """  'interface'  : %s,""", 'unicode'),
        #('score',       """  'score'      : %s,""", 'int_single_list'),
        #('pos1',        """  'pos1'       : %s,""", 'int'),
        #('pos2',        """  'pos2'       : %s,""", 'int'),
        #('subtext1',    """  'subtext1'   : %s,""", 'unicode'),
        #('subtext2',    """  'subtext2'   : %s,""", 'unicode'),
        #('monster1',    """  'monster1'   : %s,""", 'int'),
        #('monster2',    """  'monster2'   : %s,""", 'int'),
        #('shotjudge',   """  'shotjudge'  : %s,""", 'str'),
        #('skilljudge',  """  'skilljudge' : %s,""", 'str'),
        #('skillevent',  """  'skillevent' : %s,""", 'str'),
        #('eventtext',   """  'eventtext'  : %s,""", 'unicode'),
        ('guide_image', """  'guide_image': %s,""", 'str'),
        ('guide_name', """  'guide_name': %s,""", 'unicode'),
        ('guide_image2', """  'guide_image2': %s,""", 'str'),
        ('guide_orient', """  'guide_orient': %s,""", 'str'),
        ('guide_x',     """  'guide_x'    : %s,""", 'int'),
        ('guide_y',     """  'guide_y'    : %s,""", 'int'),
        ('guide_text',  """  'guide_text' : %s,""", 'unicode'),
        ('arrow_type',  """  'arrow_type' : %s,""", 'int'),
        ('arrow1_x',      """  'arrow1_x'     : %s,""", 'str'),
        ('arrow1_y',      """  'arrow1_y'     : %s,""", 'str'),
        ('arrow1_rotate', """  'arrow1_rotate': %s,""", 'str'),
        ('arrow2_x',      """  'arrow2_x'     : %s,""", 'str'),
        ('arrow2_y',      """  'arrow2_y'     : %s,""", 'str'),
        ('arrow2_rotate', """  'arrow2_rotate': %s,""", 'str'),
        ('shadow1_x',     """  'shadow1_x'    : %s,""", 'str'),
        ('shadow1_y',     """  'shadow1_y'    : %s,""", 'str'),
        ('shadow1_l',     """  'shadow1_l'    : %s,""", 'str'),
        ('shadow1_h',     """  'shadow1_h'    : %s,""", 'str'),
        ('shadow2_x',     """  'shadow2_x'    : %s,""", 'str'),
        ('shadow2_y',     """  'shadow2_y'    : %s,""", 'str'),
        ('shadow2_l',     """  'shadow2_l'    : %s,""", 'str'),
        ('shadow2_h',     """  'shadow2_h'    : %s,""", 'str'),
        ('shadow3_x',     """  'shadow3_x'    : %s,""", 'str'),
        ('shadow3_y',     """  'shadow3_y'    : %s,""", 'str'),
        ('shadow3_l',     """  'shadow3_l'    : %s,""", 'str'),
        ('shadow3_h',     """  'shadow3_h'    : %s,""", 'str'),
        ('END', """},""", 'None'),
        ], handle_funcs

def guidestreet():
    handle_funcs = {}
    handle_funcs['arrow1_x'] = lambda v: v['arrow1_x'] is not None
    handle_funcs['arrow1_y'] = lambda v: v['arrow1_y'] is not None
    handle_funcs['arrow1_rotate'] = lambda v: v['arrow1_rotate'] is not None
    handle_funcs['arrow2_x'] = lambda v: v['arrow2_x'] is not None
    handle_funcs['arrow2_y'] = lambda v: v['arrow2_y'] is not None
    handle_funcs['arrow2_rotate'] = lambda v: v['arrow2_rotate'] is not None
    handle_funcs['shadow1_x'] = lambda v: v['shadow1_x'] is not None
    handle_funcs['shadow1_y'] = lambda v: v['shadow1_y'] is not None
    handle_funcs['shadow1_l'] = lambda v: v['shadow1_l'] is not None
    handle_funcs['shadow1_h'] = lambda v: v['shadow1_h'] is not None
    handle_funcs['shadow2_x'] = lambda v: v['shadow2_x'] is not None
    handle_funcs['shadow2_y'] = lambda v: v['shadow2_y'] is not None
    handle_funcs['shadow2_l'] = lambda v: v['shadow2_l'] is not None
    handle_funcs['shadow2_h'] = lambda v: v['shadow2_h'] is not None
    handle_funcs['shadow3_x'] = lambda v: v['shadow3_x'] is not None
    handle_funcs['shadow3_y'] = lambda v: v['shadow3_y'] is not None
    handle_funcs['shadow3_l'] = lambda v: v['shadow3_l'] is not None
    handle_funcs['shadow3_h'] = lambda v: v['shadow3_h'] is not None

    return [
        ('id',  """%s: {""", 'int'),
        ('id',          """  'cfg_id'     : %s,""", 'int'),
        ('order',       """  'order'      : %s,""", 'int'),
        ('save',        """  'save'       : %s,""", 'int'),
        ('guidegroup',  """  'guidegroup' : %s,""", 'int'),
        ('is_savepoint',"""  'is_savepoint': %s,""", 'int'),
        ('is_battle',   """  'is_battle'  : %s,""", 'int'),
        ('function',    """  'function'   : %s,""", 'int'),
        #('interface',   """  'interface'  : %s,""", 'unicode'),
        #('score',       """  'score'      : %s,""", 'int_single_list'),
        #('pos1',        """  'pos1'       : %s,""", 'int'),
        #('pos2',        """  'pos2'       : %s,""", 'int'),
        #('subtext1',    """  'subtext1'   : %s,""", 'unicode'),
        #('subtext2',    """  'subtext2'   : %s,""", 'unicode'),
        #('monster1',    """  'monster1'   : %s,""", 'int'),
        #('monster2',    """  'monster2'   : %s,""", 'int'),
        #('shotjudge',   """  'shotjudge'  : %s,""", 'str'),
        #('skilljudge',  """  'skilljudge' : %s,""", 'str'),
        #('skillevent',  """  'skillevent' : %s,""", 'str'),
        #('eventtext',   """  'eventtext'  : %s,""", 'unicode'),
        ('guide_image', """  'guide_image': %s,""", 'str'),
        ('guide_name', """  'guide_name': %s,""", 'unicode'),
        ('guide_image2', """  'guide_image2': %s,""", 'str'),
        ('guide_orient', """  'guide_orient': %s,""", 'str'),
        ('guide_x',     """  'guide_x'    : %s,""", 'int'),
        ('guide_y',     """  'guide_y'    : %s,""", 'int'),
        ('guide_text',  """  'guide_text' : %s,""", 'unicode'),
        ('arrow_type',  """  'arrow_type' : %s,""", 'int'),
        ('arrow1_x',      """  'arrow1_x'     : %s,""", 'str'),
        ('arrow1_y',      """  'arrow1_y'     : %s,""", 'str'),
        ('arrow1_rotate', """  'arrow1_rotate': %s,""", 'str'),
        ('arrow2_x',      """  'arrow2_x'     : %s,""", 'str'),
        ('arrow2_y',      """  'arrow2_y'     : %s,""", 'str'),
        ('arrow2_rotate', """  'arrow2_rotate': %s,""", 'str'),
        ('shadow1_x',     """  'shadow1_x'    : %s,""", 'str'),
        ('shadow1_y',     """  'shadow1_y'    : %s,""", 'str'),
        ('shadow1_l',     """  'shadow1_l'    : %s,""", 'str'),
        ('shadow1_h',     """  'shadow1_h'    : %s,""", 'str'),
        ('shadow2_x',     """  'shadow2_x'    : %s,""", 'str'),
        ('shadow2_y',     """  'shadow2_y'    : %s,""", 'str'),
        ('shadow2_l',     """  'shadow2_l'    : %s,""", 'str'),
        ('shadow2_h',     """  'shadow2_h'    : %s,""", 'str'),
        ('shadow3_x',     """  'shadow3_x'    : %s,""", 'str'),
        ('shadow3_y',     """  'shadow3_y'    : %s,""", 'str'),
        ('shadow3_l',     """  'shadow3_l'    : %s,""", 'str'),
        ('shadow3_h',     """  'shadow3_h'    : %s,""", 'str'),
        ('END', """},""", 'None'),
        ], handle_funcs

def guidebattle():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',          """  'cfg_id'     : %s,""", 'int'),
        ('function',    """  'function'   : %s,""", 'int'),
        ('pos1',        """  'pos1'       : %s,""", 'int'),
        ('pos2',        """  'pos2'       : %s,""", 'int'),
        ('formation',   """  'formation'  : %s,""", 'int_single_list'),
        ('shotjudge',   """  'shotjudge'  : %s,""", 'int_single_list'),
        ('ctrljudge',   """  'ctrljudge'  : %s,""", 'int'),
        ('rebjudge',    """  'rebjudge'   : %s,""", 'int'),
        ('willjudge',   """  'willjudge'  : %s,""", 'int'),
        ('eventtext',   """  'eventtext'  : %s,""", 'unicode'),
        ('guide_image', """  'guide_image': %s,""", 'str'),
        ('guide_name',  """  'guide_name' : %s,""", 'unicode'),
        ('guide_image2', """  'guide_image2': %s,""", 'str'),
        ('guide_orient', """  'guide_orient': %s,""", 'str'),
        ('guide_x',     """  'guide_x'    : %s,""", 'int'),
        ('guide_y',     """  'guide_y'    : %s,""", 'int'),
        ('guide_text',  """  'guide_text' : %s,""", 'unicode'),
        ('arrow_type',  """  'arrow_type' : %s,""", 'int'),
        ('arrow1_x',      """  'arrow1_x'     : %s,""", 'str'),
        ('arrow1_y',      """  'arrow1_y'     : %s,""", 'str'),
        ('arrow1_rotate', """  'arrow1_rotate': %s,""", 'str'),
        ('arrow2_x',      """  'arrow2_x'     : %s,""", 'str'),
        ('arrow2_y',      """  'arrow2_y'     : %s,""", 'str'),
        ('arrow2_rotate', """  'arrow2_rotate': %s,""", 'str'),
        ('shadow1_x',     """  'shadow1_x'    : %s,""", 'str'),
        ('shadow1_y',     """  'shadow1_y'    : %s,""", 'str'),
        ('shadow1_l',     """  'shadow1_l'    : %s,""", 'str'),
        ('shadow1_h',     """  'shadow1_h'    : %s,""", 'str'),
        ('shadow2_x',     """  'shadow2_x'    : %s,""", 'str'),
        ('shadow2_y',     """  'shadow2_y'    : %s,""", 'str'),
        ('shadow2_l',     """  'shadow2_l'    : %s,""", 'str'),
        ('shadow2_h',     """  'shadow2_h'    : %s,""", 'str'),
        ('shadow3_x',     """  'shadow3_x'    : %s,""", 'str'),
        ('shadow3_y',     """  'shadow3_y'    : %s,""", 'str'),
        ('shadow3_l',     """  'shadow3_l'    : %s,""", 'str'),
        ('shadow3_h',     """  'shadow3_h'    : %s,""", 'str'),
        ('END', """},""", 'None'),
    ], {}

def guidebattleini():
    return [
        ('score1',      """  'score1'     : %s,""", 'int'),
        ('score2',      """  'score2'     : %s,""", 'int'),
        ('roundini',    """  'roundini'   : %s,""", 'int'),
        ('strategy1',   """  'strategy1'  : %s,""", 'int'),
        ('strategy2',   """  'strategy2'  : %s,""", 'int'),
        ('name1',       """  'name1'      : %s,""", 'unicode'),
        ('name2',       """  'name2'      : %s,""", 'unicode'),
        ('logo1',       """  'logo1'      : %s,""", 'int'),
        ('logo2',       """  'logo2'      : %s,""", 'int'),
    ], {}

def guideformation():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',          """  'cfg_id'     : %s,""", 'int'),
        ('team',        """  'team'       : %s,""", 'int'),
        ('pos',         """  'pos'        : %s,""", 'int'),
        ('monster',     """  'monster'    : %s,""", 'int'),
        ('stamina',     """  'stamina'    : %s,""", 'int'),
        ('rage',        """  'rage'       : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}

def goods_code():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',          """  'cfg_id'     : %s,""", 'int'),
        ('name',        """  'name'       : %s,""", 'unicode'),
        ('treasure',    """  'treasure'   : %s,""", 'int'),
        ('limit_start', """  'limit_start': %s,""", 'str'),
        ('limit_end',   """  'limit_end'  : %s,""", 'str'),
        ('limit_value', """  'limit_value': %s,""", 'int'),
        ('limit_user',  """  'limit_user' : %s,""", 'int'),
        ('samecode',    """  'samecode'   : %s,""", 'str'),
        ('market',      """  'market'     : %s,""", 'str'),
        ('END', """},""", 'None'),
    ], {}

def text_home():
    handle_funcs = {}
    handle_funcs['fit1'] = lambda v: v['fit1']
    handle_funcs['fit2'] = lambda v: v['fit2']
    handle_funcs['other1'] = lambda v: v['other1']
    handle_funcs['other2'] = lambda v: v['other2']
    handle_funcs['other3'] = lambda v: v['other3']
    handle_funcs['other4'] = lambda v: v['other4']
    handle_funcs['other5'] = lambda v: v['other5']

    return [
        ('pos',  """%s: {""", 'int'),
        ('unfit1', """  'unfit1': %s,""", 'unicode'),
        ('unfit2', """  'unfit2': %s,""", 'unicode'),
        ('',       """  'other' : [""", 'None'),
        ('fit1',   """             %s,""", 'unicode'),
        ('fit2',   """             %s,""", 'unicode'),
        ('other1', """             %s,""", 'unicode'),
        ('other2', """             %s,""", 'unicode'),
        ('other3', """             %s,""", 'unicode'),
        ('other4', """             %s,""", 'unicode'),
        ('other5', """             %s,""", 'unicode'),
        ('',       """           ],""", 'None'),
        ('END', """},""", 'None'),
    ], handle_funcs

def award_signday():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',              """  'id'           : %s,""", 'int'),
        ('name',            """  'name'         : %s,""", 'unicode'),
        ('award_detail',    """  'award_detail' : %s,""", 'list'),
        ('resigncost',      """  'resigncost'   : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}


def award_signday2():
    return [
        ('days',  """%s: {""", 'int'),
        ('days',         """  'days'         : %s,""", 'int'),
        ('normal',       """  'normal'       : %s,""", 'list'),
        ('luxury',       """  'luxury'       : %s,""", 'list'),
        ('cost',         """  'cost'         : %s,""", 'int'),
        ('round',        """  'round'        : %s,""", 'int'),
        ('vip',          """  'vip'          : %s,""", 'int'),
        ('image',        """  'image'        : %s,""", 'str'),
        ('END', """},""", 'None'),
    ], {}


def award_signmon():
    return [
        ('days',  """%s: {""", 'int'),
        ('days',            """  'days'               : %s,""", 'int'),
        ('award_detail',    """  'award_detail'       : %s,""", 'list'),
        ('END', """},""", 'None'),
    ], {}


def award_signnew():
    return [
        ('days',  """%s: {""", 'int'),
        ('days',            """  'days'               : %s,""", 'int'),
        ('award_detail',    """  'award_detail'       : %s,""", 'list'),
        ('END', """},""", 'None'),
    ], {}

def award_level():
    return [
        ('lv',  """%s: {""", 'int'),
        ('lv',              """  'lv'                 : %s,""", 'int'),
        ('award_detail',    """  'award_detail'       : %s,""", 'list'),
        ('END', """},""", 'None'),
    ], {}

def celebration_yao():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',          """  'id'           : %s,""", 'int'),
        ('starttime',   """  'starttime'    : %s,""", 'str'),
        ('endtime',     """  'endtime'      : %s,""", 'str'),
        ('energy',      """  'energy'       : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}

def goods_deadrefresh():
    template = [
        ('id',  """%s: {""", 'int'),
        ('id',          """  'id'      : %s,""", 'int'),
        ('',           """  'pool_list': [""", 'None'),
    ]
    for i in xrange(1, 4):
        template.extend([
        ('',               """       {""", 'None'),
        ('refresh%s' % i,  """          'refresh': %s,""", 'list'),
        ('num%s' % i,      """          'num'    : %s,""", 'int'),
        ('',               """       },""", 'None'),
        ])
    template.extend([
        ('',            """           ],""", 'None'),
        ('needdiamond', """  'needdiamond'  : %s,""", 'int'),
        ('needitem',    """  'needitem'     : %s,""", 'int'),
        ('freshtime',   """  'freshtime'    : %s,""", 'str'),
        ('END', """},""", 'None'),
        ])
    return template, {}

def goods_deaddetail():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',          """  'id'           : %s,""", 'int'),
        ('object',      """  'object'       : %s,""", 'list'),
        ('limit',       """  'limit'        : %s,""", 'int'),
        ('needhonor',   """  'needhonor'    : %s,""", 'int'),
        ('needdiamond', """  'needdiamond'  : %s,""", 'int'),
        ('sign',        """  'sign'         : %s,""", 'str'),
        ('END', """},""", 'None'),
    ], {}

def award_task():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',          """  'id'           : %s,""", 'int'),
        ('section',     """  'section'      : %s,""", 'int'),
        ('name',        """  'name'         : %s,""", 'unicode'),
        ('detail',      """  'detail'       : %s,""", 'unicode'),
        ('refresh',     """  'refresh'      : %s,""", 'int'),
        ('type',        """  'type'         : %s,""", 'int'),
        ('value1',      """  'value1'       : %s,""", 'list'),
        ('value2',      """  'value2'       : %s,""", 'int'),
        ('value3',      """  'value3'       : %s,""", 'int'),
        ('value4',      """  'value4'       : %s,""", 'list'),
        ('value5',      """  'value5'       : %s,""", 'list'),
        ('award',       """  'award'        : %s,""", 'list'),
        ('award2',      """  'award2'       : %s,""", 'list'),
        ('order',       """  'order'        : %s,""", 'int'),
        ('origin',      """  'origin'       : %s,""", 'int'),
        ('skip_sort',   """  'skip_sort'    : %s,""", 'int'),
        ('lv_limit',    """  'lv_limit'     : %s,""", 'int'),
        ('icon_image',  """  'icon_image'   : %s,""", 'str'),
        ('border_image',"""  'border_image' : %s,""", 'int'),
        ('icon_image1', """  'icon_image1'  : %s,""", 'str'),
        ('icon_image2', """  'icon_image2'  : %s,""", 'str'),
        ('icon_image3', """  'icon_image3'  : %s,""", 'str'),
        ('task_index',  """  'task_index'   : %s,""", 'list'),
        ('END', """},""", 'None'),
    ], {}

def award_dau():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',          """  'cfg_id'      : %s,""", 'int'),
        ('activeness',  """  'activeness'  : %s,""", 'list'),
        ('',            """  'award'       : [""", 'None'),
        ('award1',      """                    %s,""", 'list'),
        ('award2',      """                    %s,""", 'list'),
        ('award3',      """                    %s,""", 'list'),
        ('award4',      """                    %s,""", 'list'),
        ('award5',      """                    %s,""", 'list'),
        ('award6',      """                    %s,""", 'list'),
        ('',              """                  ],""", 'None'),
        ('max',       """  'max'           : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}

def formation_backup():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',          """  'id'           : %s,""", 'int'),
        ('name',        """  'name'         : %s,""", 'unicode'),
        ('buff',        """  'buff'         : %s,""", 'int'),
        ('attribute',   """  'attribute'    : %s,""", 'str_list'),
        ('unlocklv',    """  'unlocklv'     : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}

def pvp_gamepatch():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',          """  'cfg_id'       : %s,""", 'int'),
        ('',            """  'player': [""", 'None'),
        ('com1',        """                   %s,""", 'int'),
        ('com2',        """                   %s,""", 'int'),
        ('com3',        """                   %s,""", 'int'),
        ('com4',        """                   %s,""", 'int'),
        ('com5',        """                   %s,""", 'int'),
        ('com6',        """                   %s,""", 'int'),
        ('com7',        """                   %s,""", 'int'),
        ('com8',        """                   %s,""", 'int'),
        ('com9',        """                   %s,""", 'int'),
        ('com10',       """                   %s,""", 'int'),
        #('com11',       """                   %s,""", 'int'),
        ('',            """            ],""", 'None'),
        ('logo',        """  'logo'         : %s,""", 'int'),
        ('strategy',    """  'strategy'     : %s,""", 'int'),
        ('class',       """  'class'        : %s,""", 'int'),
        ('lv',          """  'lv'           : %s,""", 'int'),
        ('ability ',    """  'ability'      : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}


def systemfriend():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',          """  'cfg_id'       : %s,""", 'int'),
        ('name',        """  'name'         : %s,""", 'unicode'),
        ('logo',        """  'logo'         : %s,""", 'int'),
        ('gamewin',     """  'gamewin'      : %s,""", 'int'),
        ('strategy',    """  'strategy'     : %s,""", 'int'),
        ('lv',          """  'lv'           : %s,""", 'int'),
        ('',            """  'player': [""", 'None'),
        ('player1',     """                   %s,""", 'int'),
        ('player2',     """                   %s,""", 'int'),
        ('player3',     """                   %s,""", 'int'),
        ('player4',     """                   %s,""", 'int'),
        ('player5',     """                   %s,""", 'int'),
        ('player6',     """                   %s,""", 'int'),
        ('player7',     """                   %s,""", 'int'),
        ('player8',     """                   %s,""", 'int'),
        ('player9',     """                   %s,""", 'int'),
        ('player10',    """                   %s,""", 'int'),
        #('player11',    """                   %s,""", 'int'),
        ('',            """            ],""", 'None'),
        ('',            """  'rent': [""", 'None'),
        ('rent1',       """                   %s,""", 'list'),
        ('rent2',       """                   %s,""", 'list'),
        ('rent3',       """                   %s,""", 'list'),
        ('',            """          ],""", 'None'),
        ('END', """},""", 'None'),
    ], {}

def gacha_box():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',            """  'cfg_id'       : %s,""", 'int'),
        ('name',          """  'name'         : %s,""", 'unicode'),
        ('detail',        """  'detail'       : %s,""", 'unicode'),
        ('award_detail1', """  'award_detail1': %s,""", 'list'),
        ('num1',          """  'num1'         : %s,""", 'int'),
        ('award_detail2', """  'award_detail2': %s,""", 'list'),
        ('num2',          """  'num2'         : %s,""", 'int'),
        ('award_detail3', """  'award_detail3': %s,""", 'list'),
        ('num3',          """  'num3'         : %s,""", 'int'),
        ('key',           """  'key'          : %s,""", 'int'),
        ('use_max',       """  'use_max'      : %s,""", 'int'),
        ('image',         """  'image'        : %s,""", 'str'),
        ('star',          """  'star'         : %s,""", 'int'),
        ('safe_time',     """  'safe_time'    : %s,""", 'int'),
        ('safe_detail1',  """  'safe_detail1' : %s,""", 'list'),
        ('safe_num1',     """  'safe_num1'    : %s,""", 'int'),
        ('safe_tips',     """  'safe_tips'    : %s,""", 'unicode'),
        ('gachabox_index',  """  'gachabox_index'   : %s,""", 'list'),
        ('END', """},""", 'None'),
    ], {}

def pve_legendchapter():
    return [
        ('chapter_ID', """%s: {""", 'int'),
        ('chapter_ID',        """ 'cfg_id'           : %s,""", 'int'),
        ('chapter_order',     """ 'chapter_order'    : %s,""", 'int'),
        ('chapter_name',      """ 'chapter_name'     : %s,""", 'unicode'),
        ('name',              """ 'name'             : %s,""", 'unicode'),
        ('player',            """ 'player'           : %s,""", 'int'),
        ('needitem',          """ 'needitem'         : %s,""", 'int'),
        ('neednum',           """ 'neednum'          : %s,""", 'int'),
        ('dailytime',         """ 'dailytime'        : %s,""", 'int'),
        ('lockname',          """ 'lockname'         : %s,""", 'str'),
        ('lockchapter',       """ 'lockchapter'      : %s,""", 'int'),
        ('is_open',           """ 'is_open'          : %s,""", 'int'),
        ('banner',            """ 'banner'           : %s,""", 'str'),
        ('happylevel',        """ 'happylevel'       : %s,""", 'int_single_list'),
        ('happyaward',        """ 'happyaward'       : %s,""", 'list'),
        ('happyname',         """ 'happyname'        : %s,""", 'unicode_list'),
        ('chapter_deail',     """ 'chapter_deail'    : %s,""", 'unicode'),
        ('chapter_lootshow',  """ 'chapter_lootshow' : %s,""", 'unicode'),
        ('lootshow',          """ 'lootshow'         : %s,""", 'list'),
        ('chapter_image',     """ 'chapter_image'    : %s,""", 'int'),
        ('chapter_game',      """ 'chapter_game'     : %s,""", 'int'),
        ('chapter_card',      """ 'chapter_card'     : %s,""", 'str'),
        ('certain_value',     """ 'certain_value'    : %s,""", 'unicode'),
        ('chapter_lock',      """ 'chapter_lock'     : %s,""", 'unicode'),
        ('END', """},""", 'None'),
        ], {}

def user_functrl():
    return [
        ('id', """%s: {""", 'int'),
        ('lv',          """ 'lv'         : %s,""", 'int'),
        ('stage',       """ 'stage'      : %s,""", 'int'),
        ('text',        """ 'text'       : %s,""", 'unicode'),
        ('unlocktitle', """ 'unlocktitle': %s,""", 'unicode'),
        ('unlocktext',  """ 'unlocktext' : %s,""", 'unicode'),
        ('unlockimage', """ 'unlockimage': %s,""", 'str'),
        ('funname',     """ 'funname'    : %s,""", 'str'),
        ('is_guide',    """ 'is_guide'   : %s,""", 'int'),
        ('guide_id',    """ 'guide_id'   : %s,""", 'list'),
        ('guide_loot',  """ 'guide_loot' : %s,""", 'list'),
        ('user_loot1',  """ 'user_loot1' : %s,""", 'list'),
        ('user_loot2',  """ 'user_loot2' : %s,""", 'list'),
        ('user_loot3',  """ 'user_loot3' : %s,""", 'list'),
        ('user_loot4',  """ 'user_loot4' : %s,""", 'list'),
        ('user_loot5',  """ 'user_loot5' : %s,""", 'list'),
        ('END', """},""", 'None'),
        ], {}

def pve_dynastydetail():
    return [
        ('team_id', """%s: {""", 'int'),
        ('team_id',      """ 'cfg_id'     : %s,""", 'int'),
        ('stage_id',     """ 'stage_id'   : %s,""", 'int'),
        ('is_boss',      """ 'is_boss'    : %s,""", 'int'),
        ('chapter',      """ 'chapter'    : %s,""", 'int'),
        ('stagename',    """ 'stagename'  : %s,""", 'unicode'),
        ('chaptername',  """ 'chaptername': %s,""", 'unicode'),
        ('ability',      """ 'ability'    : %s,""", 'single_list'),
        ('lv',           """ 'lv'         : %s,""", 'single_list'),
        ('',             """  'player'    : [""", 'None'),
        ('player1',      """                   %s,""", 'int'),
        ('player2',      """                   %s,""", 'int'),
        ('player3',      """                   %s,""", 'int'),
        ('player4',      """                   %s,""", 'int'),
        ('player5',      """                   %s,""", 'int'),
        ('player6',      """                   %s,""", 'int'),
        ('player7',      """                   %s,""", 'int'),
        ('player8',      """                   %s,""", 'int'),
        ('player9',      """                   %s,""", 'int'),
        ('player10',     """                   %s,""", 'int'),
        ('',             """                ],""", 'None'),
        ('star1_range',  """ 'star1_range' : %s,""", 'int_single_list'),
        ('star1_loot',   """ 'star1_loot'  : %s,""", 'int'),
        ('star2_range',  """ 'star2_range' : %s,""", 'int_single_list'),
        ('star2_loot',   """ 'star2_loot'  : %s,""", 'int'),
        ('star3_range',  """ 'star3_range' : %s,""", 'int_single_list'),
        ('star3_loot',   """ 'star3_loot'  : %s,""", 'int'),
        ('lootfirst',    """ 'lootfirst'   : %s,""", 'int'),
        ('lootnormal',   """ 'lootnormal'  : %s,""", 'int'),
        ('superskill',   """ 'superskill'  : %s,""", 'int'),
        ('lootshow',     """ 'lootshow'    : %s,""", 'list'),
        ('END', """},""", 'None'),
        ], {}

def league_build():
    return [
        ('lv',          """  'lv'          : %s,""", 'int'),
        ('money',       """  'money'       : %s,""", 'int'),
        ('diamond',     """  'diamond'     : %s,""", 'int'),
        ('applymax',    """  'applymax'    : %s,""", 'int'),
        ('devotetime',  """  'devotetime'  : %s,""", 'int'),
        ('quitlimit',   """  'quitlimit'   : %s,""", 'int'),
        ('change_name', """  'change_name' : %s,""", 'int'),
    ], {}

def league_info():
    return [
        ('lv',  """%s: {""", 'int'),
        ('lv',               """  'cfg_id'           : %s,""", 'int'),
        ('exp',              """  'exp'              : %s,""", 'int'),
        ('maxmember',        """  'maxmember'        : %s,""", 'int'),
        ('playoffmember',    """  'playoffmember'    : %s,""", 'int'),
        ('maxapplication',   """  'maxapplication'   : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}

def league_worship():
    return [
        ('lv',  """%s: {""", 'int'),
        ('lv',              """  'cfg_id'           : %s,""", 'int'),
        ('exp',             """  'exp'              : %s,""", 'int'),
        ('starttime',       """  'starttime'        : %s,""", 'str'),
        ('endtime',         """  'endtime'          : %s,""", 'str'),
        ('description1',    """  'description1'     : %s,""", 'unicode'),
        ('description2',    """  'description2'     : %s,""", 'unicode'),
        ('loot',            """  'loot'             : %s,""", 'list'),
        ('cost_devote',     """  'cost_devote'      : %s,""", 'int'),
        ('num_devote',      """  'num_devote'       : %s,""", 'int'),
        ('cost_diamond',    """  'cost_diamond'     : %s,""", 'int'),
        ('num_diamond',     """  'num_diamond'      : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}

def league_donate():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',              """  'cfg_id'           : %s,""", 'int'),
        ('name',            """  'name'             : %s,""", 'unicode'),
        ('cost_money',      """  'cost_money'       : %s,""", 'int'),
        ('cost_diamond',    """  'cost_diamond'     : %s,""", 'int'),
        ('is_open',         """  'is_open'          : %s,""", 'int'),
        ('exp',             """  'exp'              : %s,""", 'int'),
        ('devote',          """  'devote'           : %s,""", 'int'),
        ('image',           """  'image'            : %s,""", 'str'),
        ('END', """},""", 'None'),
    ], {}


def goods_leaguedetail():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',              """  'cfg_id'           : %s,""", 'int'),
        ('object',          """  'object'           : %s,""", 'list'),
        ('num',             """  'num'              : %s,""", 'int'),
        ('sharelimit',      """  'sharelimit'       : %s,""", 'int'),
        ('needdevote',      """  'needdevote'       : %s,""", 'int'),
        ('diamond',         """  'diamond'          : %s,""", 'int'),
        ('needlv',          """  'needlv'           : %s,""", 'int'),
        ('is_fresh',        """  'is_fresh'         : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}


def goods_leaguefresh():
    return [
        ('shop_lv',  """%s: {""", 'int'),
        ('shop_lv',             """  'cfg_id'           : %s,""", 'int'),
        ('',                    """  'refresh': [   """, 'None'),
        (('refresh1', 'num1'),  """      (%s, %s),""", ('list', 'int')),
        (('refresh2', 'num2'),  """      (%s, %s),""", ('list', 'int')),
        (('refresh3', 'num3'),  """      (%s, %s),""", ('list', 'int')),
        ('',                    """  ],             """, 'None'),
        ('freshtime',           """  'freshtime'        : %s,""", 'str'),
        ('exp',                 """  'exp'              : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}


def goods_dynastydetail():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',               """  'cfg_id'       : %s,""", 'int'),
        ('object',           """  'object'       : %s,""", 'list'),
        ('limit',            """  'limit'        : %s,""", 'int'),
        ('needhonor',        """  'needhonor'    : %s,""", 'int'),
        ('diamond',          """  'diamond'      : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}

def goods_dynastyrefresh():
    template = [
        ('id',  """%s: {""", 'int'),
        ('id',         """  'cfg_id'   : %s,""", 'int'),
        ('',           """  'pool_list': [""", 'None'),
    ]
    for i in xrange(1, 4):
        template.extend([
        ('',               """       {""", 'None'),
        ('refresh%s' % i,  """          'refresh': %s,""", 'list'),
        ('num%s' % i,      """          'num'    : %s,""", 'int'),
        ('',               """       },""", 'None'),
        ])
    template.extend([
        ('',           """           ],""", 'None'),
        ('costrow',    """  'costrow'  : %s,""", 'int'),
        ('freshtime',  """  'freshtime': %s,""", 'str'),
        ('END', """},""", 'None'),
        ])
    return template, {}

def text_warning():
    return [
        (('id', 'textwarning'), """%s: %s,""", ('int', 'unicode')),
        ], {}

def gamesuperskill():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',         """  'id'        : %s,""", 'int'),
        ('superrow',   """  'superrow'  : %s,""", 'list'),
        ('ini',        """  'ini'       : %s,""", 'int'),
        ('max',        """  'max'       : %s,""", 'int'),
        ('min',        """  'min'       : %s,""", 'int'),
        ('normal',     """  'normal'    : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}

def user_ini():
    return [
        ('ini_loot',                """  'ini_loot'                 : %s,""", 'list'),
        ('equip_multi',             """  'equip_multi'              : %s,""", 'float'),
        ('energy_grow',             """  'energy_grow'              : %s,""", 'int'),
        ('battlepoint_grow',        """  'battlepoint_grow'         : %s,""", 'int'),
        ('energy_itemup',           """  'energy_itemup'            : %s,""", 'int'),
        ('battlepoint_itemup',      """  'battlepoint_itemup'       : %s,""", 'int'),
        ('push_award',              """  'push_award'               : %s,""", 'list'),
    ], {}

def goods_money():
    return [
        ('id',  """%s: {""", 'int'),
        ('money',         """  'money'      : %s,""", 'int'),
        ('cost',          """  'cost'       : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}

def pve_moneystage():
    return [
        ('id', """%s: {""", 'int'),
        ('id',              """ 'cfg_id'       : %s,""", 'int'),
        ('chapter_ID',      """ 'chapter_ID'   : %s,""", 'int'),
        ('chapter_order',   """ 'chapter_order': %s,""", 'int'),
        ('chapter_name',    """ 'chapter_name' : %s,""", 'unicode'),
        ('name',            """ 'name'         : %s,""", 'unicode'),
        ('dailytime',       """ 'dailytime'    : %s,""", 'int'),
        ('is_open',         """ 'is_open'      : %s,""", 'int'),
        ('chapter_image',   """ 'chapter_image': %s,""", 'str'),
        ('banner',          """ 'banner'       : %s,""", 'str'),
        ('level',           """ 'level'        : %s,""", 'int'),
        ('gamedetail',      """ 'gamedetail'   : %s,""", 'int'),
        ('stage_image',     """ 'stage_image'  : %s,""", 'str'),
        ('stage_border',    """ 'stage_border' : %s,""", 'str'),
        ('item',            """ 'item'         : %s,""", 'int'),
        ('chapter_tips',    """ 'chapter_tips' : %s,""", 'unicode'),
        ('chapter_sort',    """ 'chapter_sort' : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def pvp_ranking():
    return [
        ('ranking_ID',  """%s: {""", 'int'),
        ('ranking_ID',      """ 'cfg_id'       : %s,""", 'int'),
        ('sort',            """ 'sort'         : %s,""", 'int'),
        ('tag_name',        """ 'tag_name'     : %s,""", 'unicode'),
        ('information',     """ 'information'  : %s,""", 'unicode'),
        ('END',         """},""", 'None'),
    ], {}

def pvp_sectionvs():
    return [
        ('id', """%s: {""", 'int'),
        ('id',            """ 'cfg_id'       : %s,""", 'int'),
        ('section_name',  """ 'section_name' : %s,""", 'unicode'),
        ('npc_detail',    """ 'npc_detail'   : %s,""", 'list'),
        ('npc_num',       """ 'npc_num'      : %s,""", 'int'),
        ('up_num',        """ 'up_num'       : %s,""", 'int'),
        ('down_num',      """ 'down_num'     : %s,""", 'int'),
        ('is_solo',       """ 'is_solo'      : %s,""", 'int'),
        ('total_num',     """ 'total_num'    : %s,""", 'int'),
        ('section_num',   """ 'section_num'  : %s,""", 'int'),
        #('friendplus',    """ 'friendplus'   : %s,""", 'float'),
        #('moneybase',     """ 'moneybase'    : %s,""", 'int'),
        #('moneytime',     """ 'moneytime'    : %s,""", 'int'),
        #('champion_buff', """ 'champion_buff': %s,""", 'float'),
        ('refreshtime',   """ 'refreshtime'  : %s,""", 'int'),
        ('',              """ 'range'        : [""", 'None'),
        ('range1',        """                   %s,""", 'list'),
        ('range2',        """                   %s,""", 'list'),
        ('range3',        """                   %s,""", 'list'),
        ('range4',        """                   %s,""", 'list'),
        ('',              """                  ],""", 'None'),
        ('inirank',       """ 'inirank'      : %s,""", 'int'),
        ('termname',      """ 'termname'     : %s,""", 'unicode_list'),
        ('battlecost',    """ 'battlecost'   : %s,""", 'int'),
        ('winexplv',      """ 'winexplv'     : %s,""", 'float'),
        ('winexpbase',    """ 'winexpbase'   : %s,""", 'int'),
        ('loseexplv',     """ 'loseexplv'    : %s,""", 'float'),
        ('loseexpbase',   """ 'loseexpbase'  : %s,""", 'int'),
        ('order',         """ 'order'        : %s,""", 'int'),
        ('bonus',         """ 'bonus'        : %s,""", 'int'),
        #('bonusname',     """ 'bonusname'    : %s,""", 'unicode'),
        ('bonusnum',      """ 'bonusnum'     : %s,""", 'list'),
        ('',              """ 'bonusreward'  : [""", 'None'),
        ('bonusreward1',  """                    %s,""", 'list'),
        ('bonusreward2',  """                    %s,""", 'list'),
        ('bonusreward3',  """                    %s,""", 'list'),
        ('bonusreward4',  """                    %s,""", 'list'),
        ('',              """                  ],""", 'None'),
        ('END', """},""", 'None'),
        ], {}

def pvp_gamevs():
    return [
        ('npc_id', """%s: {""", 'int'),
        ('npc_id',      """ 'cfg_id'    : %s,""", 'int'),
        ('name',        """ 'name'      : %s,""", 'unicode'),
        ('lv',          """ 'lv'        : %s,""", 'int'),
        ('logo',        """ 'logo'      : %s,""", 'int'),
        ('strategy',    """ 'strategy'  : %s,""", 'int'),
        ('',            """  'player'   : [""", 'None'),
        ('player1',     """                   %s,""", 'int'),
        ('player2',     """                   %s,""", 'int'),
        ('player3',     """                   %s,""", 'int'),
        ('player4',     """                   %s,""", 'int'),
        ('player5',     """                   %s,""", 'int'),
        ('player6',     """                   %s,""", 'int'),
        ('player7',     """                   %s,""", 'int'),
        ('player8',     """                   %s,""", 'int'),
        ('player9',     """                   %s,""", 'int'),
        ('player10',    """                   %s,""", 'int'),
        ('',            """            ],""", 'None'),
        ('winexplv',    """ 'winexplv'   : %s,""", 'int'),
        ('loseexplv',   """ 'loseexplv'  : %s,""", 'int'),
        ('rank',        """ 'rank'       : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def pvp_kvs():
    return [
        ('id', """%s: {""", 'int'),
        ('id',       """ 'cfg_id'  : %s,""", 'int'),
        ('range',    """ 'range'   : %s,""", 'list'),
        ('b',        """ 'b'       : %s,""", 'int'),
        ('a',        """ 'a'       : %s,""", 'float'),
        ('r0',       """ 'r0'      : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def award_vsrankseason():
    return [
        ('id', """%s: {""", 'int'),
        ('id',          """ 'cfg_id'     : %s,""", 'int'),
        ('start_rank',  """ 'start_rank' : %s,""", 'int'),
        ('end_rank',    """ 'end_rank'   : %s,""", 'int'),
        ('round_award', """ 'round_award': %s,""", 'list'),
        ('section_vs',  """ 'section_vs' : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def award_vsrankwin():
    return award_vsrankseason()

def award_vsturnloot():
    return [
        ('id', """%s: {""", 'int'),
        ('id',          """ 'cfg_id'    : %s,""", 'int'),
        ('section',      """ 'section'  : %s,""", 'int'),
        ('rank',         """ 'rank'     : %s,""", 'json'),
        ('loot',         """ 'loot'     : %s,""", 'list'),
        ('lootshow',     """ 'lootshow' : %s,""", 'list'),
        ('loot_tip',     """ 'loot_tip' : %s,""", 'unicode'),
        ('END', """},""", 'None'),
        ], {}

def award_sp():
    return [
        ('token', """%s: {""", 'str'),
        ('uid',           """ 'uid'          : %s,""", 'str'),
        ('username',      """ 'username'     : %s,""", 'unicode'),
        ('level',         """ 'level'        : %s,""", 'int'),
        ('arena_rank',    """ 'arena_rank'   : %s,""", 'int'),
        ('ability_rank',  """ 'ability_rank' : %s,""", 'int'),
        ('open_chapters', """ 'open_chapters': %s,""", 'json'),
        ('login_days',    """ 'login_days'   : %s,""", 'json'),
        ('code_ids',      """ 'code_ids'     : %s,""", 'json'),
        ('END', """},""", 'None'),
        ], {}

def award_sp2():
    return [
        ('token', """%s: {""", 'str'),
        ('uid',           """ 'uid'          : %s,""", 'str'),
        #('username',      """ 'username'     : %s,""", 'json'),
        ('level',         """ 'level'        : %s,""", 'int'),
        ('level_rank',    """ 'level_rank'   : %s,""", 'int'),
        ('pay_days',      """ 'pay_days'     : %s,""", 'int'),
        ('pay_rmbs',      """ 'pay_rmbs'     : %s,""", 'int'),
        ('item',          """ 'item'         : %s,""", 'json'),
        #('code_ids',      """ 'code_ids'     : %s,""", 'json'),
        ('END', """},""", 'None'),
        ], {}

def award_sp3():
    return [
        ('token', """%s: {""", 'str'),
        ('uid',           """ 'uid'          : %s,""", 'str'),
        #('username',      """ 'username'     : %s,""", 'json'),
        ('pay_days',      """ 'pay_days'     : %s,""", 'int'),
        ('pay_rmbs',      """ 'pay_rmbs'     : %s,""", 'int'),
        ('item',          """ 'item'         : %s,""", 'json'),
        #('code_ids',      """ 'code_ids'     : %s,""", 'json'),
        ('END', """},""", 'None'),
        ], {}

def award_sp4():
    return [
        ('token', """%s: {""", 'str'),
        ('uid',           """ 'uid'          : %s,""", 'str'),
        #('username',      """ 'username'     : %s,""", 'json'),
        ('item',          """ 'item'         : %s,""", 'json'),
        #('code_ids',      """ 'code_ids'     : %s,""", 'json'),
        ('END', """},""", 'None'),
        ], {}

def goods_vs():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',           """  'cfg_id'      : %s,""", 'int'),
        ('name',         """  'name'        : %s,""", 'unicode'),
        ('description',  """  'description' : %s,""", 'unicode'),
        ('order',        """  'order'       : %s,""", 'int'),
        ('limit_type',   """  'limit_type'  : %s,""", 'int'),
        ('limit_value1', """  'limit_value1': %s,""", 'int'),
        ('limit_value2', """  'limit_value2': %s,""", 'int'),
        ('is_open',      """  'is_open'     : %s,""", 'int'),
        ('honor_cost',   """  'honor_cost'  : %s,""", 'int'),
        ('loot',         """  'loot'        : %s,""", 'list'),
        ('END', """},""", 'None'),
        ], {}

def pvp_gamevs2():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',        """  'cfg_id'   : %s,""", 'int'),
        ('up_down',   """  'up_down'  : %s,""", 'int'),
        ('',          """  'vs'       : [""", 'None'),
        ('vs1',       """                %s,""", 'json'),
        ('vs2',       """                %s,""", 'json'),
        ('vs3',       """                %s,""", 'json'),
        ('vs4',       """                %s,""", 'json'),
        ('vs5',       """                %s,""", 'json'),
        ('',          """              ],""", 'None'),
        ('lootwin',   """  'lootwin'  : %s,""", 'list'),
        ('lootlose',  """  'lootlose' : %s,""", 'list'),
        ('judgewin',  """  'judgewin' : %s,""", 'int'),
        ('judgelose', """  'judgelose': %s,""", 'int'),
        ('npcini',    """  'npcini'   : %s,""", 'int_single_list'),
        ('npcscore',  """  'npcscore' : %s,""", 'int_single_list'),
        ('vs_text',   """  'vs_text'  : %s,""", 'unicode'),
        ('rankingini',  """  'rankingini'   : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def activity_diamond():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',                  """  'cfg_id'      : %s,""", 'int'),
        ('same_arm',            """  'same_arm'    : %s,""", 'int'),
        ('diamond_show',        """  'diamond_show': %s,""", 'list'),
        ('need_diamond',        """  'need_diamond': %s,""", 'int'),
        ('time',                """  'time'        : %s,""", 'int'),
        ('',                    """  'class_weight': [""", 'None'),
        (('classA', 'weightA'), """                  (%s,%s),""", ('json', 'int')),
        (('classB', 'weightB'), """                  (%s,%s),""", ('json', 'int')),
        (('classC', 'weightC'), """                  (%s,%s),""", ('json', 'int')),
        ('',                    """                 ],""", 'None'),
        ('END', """},""", 'None'),
        ], {}

def pve_hchapter():
    return [
        ('chapter_ID', """%s: {""", 'int'),
        ('chapter_ID',        """ 'cfg_id'       : %s,""", 'int'),
        ('chapter_order',     """ 'chapter_order': %s,""", 'int'),
        ('chapter_name',      """ 'chapter_name' : %s,""", 'unicode'),
        ('chapter_level',     """ 'chapter_level': %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}

def pve_hstage():
    return [
        ('stage_ID', """%s: {""", 'int'),
        ('stage_ID',          """ 'cfg_id'           : %s,""", 'int'),
        ('chapter_ID',        """ 'chapter_ID'       : %s,""", 'int'),
        ('chapter_name',      """ 'chapter_name'     : %s,""", 'unicode'),
        ('stage_order',       """ 'stage_order'      : %s,""", 'int'),
        ('energycost',        """ 'energycost'       : %s,""", 'int'),
        ('unlockstages',      """ 'unlockstages'     : %s,""", 'int'),
        ('stage_name',        """ 'stage_name'       : %s,""", 'unicode'),
        ('stage_description', """ 'stage_description': %s,""", 'unicode'),
        ('certainloot',       """ 'certainloot'      : %s,""", 'int'),
        ('certain_value',     """ 'certain_value'    : %s,""", 'unicode'),
        ('stage_dailylimit',  """ 'stage_dailylimit' : %s,""", 'int'),
        ('stage_lootshow',    """ 'stage_lootshow'   : %s,""", 'list'),
        ('firstlootshow',     """ 'firstlootshow'    : %s,""", 'list'),
        ('level',             """ 'level'            : %s,""", 'int'),
        ('stage_sort',        """ 'stage_sort'       : %s,""", 'int'),
        ('stage_image',       """ 'stage_image'      : %s,""", 'str'),
        ('stage_border',      """ 'stage_border'     : %s,""", 'str'),
        ('stage_team',        """ 'stage_team'       : %s,""", 'str'),
        ('is_boss',           """ 'is_boss'          : %s,""", 'str'),
        ('energy_cost1',      """ 'energy_cost1'     : %s,""", 'int'),
        ('energy_cost2',      """ 'energy_cost2'     : %s,""", 'int'),
        ('stage_reset',       """ 'stage_reset'      : %s,""", 'int'),
        ('game_id',           """ 'game_id'          : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}


def player_tutor():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',              """   'cfg_id'          : %s,""", 'int'),
        ('sametutor',       """   'sametutor'       : %s,""", 'int'),
        ('star',            """   'star'            : %s,""", 'int'),
        ('starplus',        """   'starplus'        : %s,""", 'int'),
        ('starlevel',       """   'starlevel'       : %s,""", 'int'),
        ('name',            """   'name'            : %s,""", 'unicode'),
        ('image',           """   'image'           : %s,""", 'str'),
        ('',                """ 'init': {""", 'None'),
        ('pt3_int',         """              'pt3'  : %s,""", 'int'),
        ('pt2_ini',         """              'pt2'  : %s,""", 'int'),
        ('layup_ini',       """              'layup': %s,""", 'int'),
        ('steal_ini',       """              'steal': %s,""", 'int'),
        ('inter_ini',       """              'inter': %s,""", 'int'),
        ('block_ini',       """              'block': %s,""", 'int'),
        ('',                """         },""", 'None'),
        ('',                """ 'show': {""", 'None'),
        ('pt3_show',        """              'pt3'  : %s,""", 'int'),
        ('pt2_show',        """              'pt2'  : %s,""", 'int'),
        ('layup_show',      """              'layup': %s,""", 'int'),
        ('steal_show',      """              'steal': %s,""", 'int'),
        ('inter_show',      """              'inter': %s,""", 'int'),
        ('block_show',      """              'block': %s,""", 'int'),
        ('',                """         },""", 'None'),
        ('',                """ 'item': [""", 'None'),
        ('item1',   """              %s,""", 'int'),
        ('item2',   """              %s,""", 'int'),
        ('item3',   """              %s,""", 'int'),
        ('item4',   """              %s,""", 'int'),
        ('item5',   """              %s,""", 'int'),
        ('item6',   """              %s,""", 'int'),
        ('',                """            ],""", 'None'),
        ('needmoney',        """   'needmoney'       : %s,""", 'int'),
        ('evo_tip',          """   'evo_tip'         : %s,""", 'unicode'),
        ('END', """},""", 'None'),
    ], {}


def item_merge():
    return [
        ('merge_id', """%s: {""", 'int'),
        ('merge_id',        """ 'cfg_id'        : %s,""", 'int'),
        ('name',            """ 'name'          : %s,""", 'unicode'),
        ('item',            """ 'item'          : %s,""", 'list'),
        ('object_item',     """ 'object_item'   : %s,""", 'int'),
        ('merge_money',     """ 'merge_money'   : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}


def patchitem():
    return [
        ('patchitem_id', """%s: {""", 'int'),
        ('patchitem_id',    """ 'cfg_id'        : %s,""", 'int'),
        ('exchange_num',    """ 'exchange_num'  : %s,""", 'int'),
        ('object_item',     """ 'object_item'   : %s,""", 'int'),
        ('money_cost',      """ 'money_cost'    : %s,""", 'int'),
        ('name',            """ 'name'          : %s,""", 'unicode'),
        ('END', """},""", 'None'),
    ], {}

def activity_roulettefresh():
    return [
        ('id', """%s: {""", 'int'),
        ('id',              """  'cfg_id'            : %s,""", 'int'),
        ('same_roulette',   """  'same_roulette'     : %s,""", 'int'),
        ('show_sort',       """  'show_sort'         : %s,""", 'int'),
        ('fresh_detail',    """  'fresh_detail'      : %s,""", 'list'),
        ('safe_detail',     """  'safe_detail'       : %s,""", 'list'),
        ('safe_num',        """  'safe_num'          : %s,""", 'int'),
        ('free',            """  'free'              : %s,""", 'int'),
        ('cost_diamond1',   """  'cost_diamond1'     : %s,""", 'int'),
        ('cost_diamond10',  """  'cost_diamond10'    : %s,""", 'int'),
        ('cost_item',       """  'cost_item'         : %s,""", 'list'),
        ('cost_item10',     """  'cost_item10'       : %s,""", 'list'),
        ('',                """  'fresh_time'        : [""", 'None'),
        ('fresh_time1',     """                        %s,""", 'str'),
        ('fresh_time2',     """                        %s,""", 'str'),
        ('fresh_time3',     """                        %s,""", 'str'),
        ('',                """                      ],""", 'None'),
        ('round',           """  'round'             : %s,""", 'int'),
        ('gift1',           """  'gift1'             : %s,""", 'int'),
        ('gift10',          """  'gift10'            : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}


def activity_roulette():
    handle_funcs = {}
    # handle_funcs[('gacha_detail1', 'num1')] = lambda v: v['num1']
    # handle_funcs[('gacha_detail2', 'num2')] = lambda v: v['num2']
    # handle_funcs[('gacha_detail3', 'num3')] = lambda v: v['num3']
    # handle_funcs[('gacha_detail4', 'num4')] = lambda v: v['num4']

    return [
        ('id',  """%s: {""", 'int'),
        ('id',            """  'cfg_id'        : %s,""", 'int'),
        ('gacha_sort',    """  'gacha_sort'    : %s,""", 'int'),
        ('',              """  'gacha_detail': [""", 'None'),
        (('gacha_detail1', 'num1'), """          (%s, %s),""", ('list', 'int')),
        (('gacha_detail2', 'num2'), """          (%s, %s),""", ('list', 'int')),
        (('gacha_detail3', 'num3'), """          (%s, %s),""", ('list', 'int')),
        (('gacha_detail4', 'num4'), """          (%s, %s),""", ('list', 'int')),
        ('',                     """        ],""", 'None'),
        ('',              """  'percent'       : [""", 'None'),
        ('percent1',      """                    %s,""", 'int'),
        ('percent2',      """                    %s,""", 'int'),
        ('percent3',      """                    %s,""", 'int'),
        ('percent4',      """                    %s,""", 'int'),
        ('',              """                  ],""", 'None'),
        ('',              """  'percent_item'  : [""", 'None'),
        ('percent1_item', """                    %s,""", 'int'),
        ('percent2_item', """                    %s,""", 'int'),
        ('percent3_item', """                    %s,""", 'int'),
        ('percent4_item', """                    %s,""", 'int'),
        ('',              """                  ],""", 'None'),
        ('',              """  'percent_free'  : [""", 'None'),
        ('percent1_free', """                    %s,""", 'int'),
        ('percent2_free', """                    %s,""", 'int'),
        ('percent3_free', """                    %s,""", 'int'),
        ('percent4_free', """                    %s,""", 'int'),
        ('',              """                  ],""", 'None'),
        ('safe_num1',     """  'safe_num1'     : %s,""", 'int'),
        ('goods_sp',      """  'goods_sp'      : %s,""", 'list'),
        ('END', """},""", 'None'),
    ], handle_funcs


def goods_roulette():
    return [
        ('id',  """%s: {""", 'int'),
        ('id',                 """  'cfg_id'             : %s,""", 'int'),
        ('same_goodsroulette', """  'same_goodsroulette' : %s,""", 'int'),
        ('object',             """  'object'             : %s,""", 'list'),
        ('sharelimit',         """  'sharelimit'         : %s,""", 'int'),
        ('num',                """  'num'                : %s,""", 'int'),
        ('needgift',           """  'needgift'           : %s,""", 'int'),
        ('order',              """  'order'              : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}


def text_getshow():
    return [
        ('id', """%s: {""", 'int'),
        ('id',         """ 'cfg_id'    : %s,""", 'int'),
        ('title',      """ 'title'     : %s,""", 'unicode'),
        ('sort',       """ 'sort'      : %s,""", 'int'),
        ('name',       """ 'name'      : %s,""", 'unicode'),
        ('detail',     """ 'detail'    : %s,""", 'int'),
        ('skip_sort',  """ 'skip_sort' : %s,""", 'int'),
        ('END', """},""", 'None'),
        ], {}



def award_fund():
    return [
        ('id', """%s: {""", 'int'),
        ('id',      """ 'cfg_id'        : %s,""", 'int'),
        ('lv',      """ 'lv'            : %s,""", 'int'),
        ('diamond', """ 'diamond'       : %s,""", 'int'),
        ('name',    """ 'name'          : %s,""", 'unicode'),
        ('text',    """ 'text'          : %s,""", 'unicode'),
        ('image',   """ 'image'         : %s,""", 'str'),
        ('icon',    """ 'icon'          : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}


def strategy_emblem():
    return [
        ('strategy', """%s: {""", 'int'),
        ('strategy',        """ 'cfg_id'        : %s,""", 'int'),
        ('samestrategy',    """ 'samestrategy'  : %s,""", 'int'),
        ('star',            """ 'star'          : %s,""", 'int'),
        ('name',            """ 'name'          : %s,""", 'unicode'),
        ('ability',         """ 'ability'       : %s,""", 'int'),
        ('emblem_x',        """ 'emblem_x'      : %s,""", 'int'),
        ('emblem_y',        """ 'emblem_y'      : %s,""", 'int'),
        ('emblem_z',        """ 'emblem_z'      : %s,""", 'int'),
        ('emblem_unlock',   """ 'emblem_unlock' : %s,""", 'int'),
        ('emblem_tip',      """ 'emblem_tip'    : %s,""", 'unicode'),
        ('image',           """ 'image'         : %s,""", 'str'),
        ('END', """},""", 'None'),
    ], {}


def award_arenafirst():
    return [
        ('id', """%s: {""", 'int'),
        ('id',              """ 'cfg_id'        : %s,""", 'int'),
        ('start_rank',      """ 'start_rank'    : %s,""", 'int'),
        ('end_rank',        """ 'end_rank'      : %s,""", 'int'),
        ('award_loot',      """ 'award_loot'    : %s,""", 'list'),
        ('over_num',        """ 'over_num'      : %s,""", 'int'),
        ('END', """},""", 'None'),
    ], {}


def type_diamond():
    return [
        ('chance',          """  'chance'       : %s,""", 'list'),
    ], {}


def loot_double():
    return [
        ('id', """%s: {""", 'int'),
        ('id',              """ 'cfg_id'            : %s,""", 'int'),
        ('object_sort',     """ 'object_sort'       : %s,""", 'int'),
        ('object_stage',    """ 'object_stage'      : %s,""", 'list'),
        ('show_sort',       """ 'show_sort'         : %s,""", 'int'),
        ('exp_times',       """ 'exp_times'         : %s,""", 'float'),
        ('money_times',     """ 'money_times'       : %s,""", 'float'),
        ('diamond_times',   """ 'diamond_times'     : %s,""", 'float'),
        ('other_times',     """ 'other_times'       : %s,""", 'float'),
        ('cycle_detail',    """ 'cycle_detail'      : %s,""", 'int'),
        ('time_start',      """ 'time_start'        : %s,""", 'str'),
        ('time_end',        """ 'time_end'          : %s,""", 'str'),
        ('server_id',       """ 'server_id'         : %s,""", 'int_single_list'),
        ('END', """},""", 'None'),
    ], {}
