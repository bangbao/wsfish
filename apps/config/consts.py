# coding: utf-8


def servers_func(game_config, config_name, config_value):
    pass
#     import settings
#     for server_id, obj in config_value.iteritems():
#         settings.SERVERS[server_id] = {'db_index': obj.get('db_index', 0),
#                                        'db_key': obj.get('db_key', '')}
#     # 设定默认的分服db设置
#     if '00' not in settings.SERVERS:
#         settings.SERVERS['00'] = {'db_index': 0, 'db_key': ''}

def charge_func(game_config, config_name, config_value):
    """充值定单配置，额外增加商品id到配置的映射配置
    """
    data = {}
    open_gifts = {}
    for buy_id, obj in config_value.iteritems():
        data[obj['cost']] = buy_id
        open_gifts.setdefault(obj['open_gift'], []).append(buy_id)
    setattr(game_config, 'charge_scheme', data)
    setattr(game_config, 'charge_open_gift', open_gifts)

def user_info_func(game_config, config_name, config_value):
    rent_num_openlv = {}
    for level, obj in sorted(config_value.iteritems()):
        if obj['rent_num'] not in rent_num_openlv:
            rent_num_openlv[obj['rent_num']] = level
    setattr(game_config, 'rent_num_openlv', rent_num_openlv)

def player_detail_func(game_config, config_name, config_value):
    all_player_detail = getattr(game_config, 'player_detail', {})
    all_player_detail.update(config_value)
    starlevel_data = {}
    starplus_data = {}
    material_sort_data = {}
    for cfg_id, obj in all_player_detail.iteritems():
        temp = starlevel_data.setdefault(obj['sameevolution'], {})
        temp[obj['starlevel']] = cfg_id
        temp2 = starplus_data.setdefault(obj['sameevolution'], {}).setdefault(obj['star'], {})
        temp2[obj['starplus']] = cfg_id
        temp3 = material_sort_data.setdefault(obj['material_sort'], {})
        temp3[obj['star']] = cfg_id
    setattr(game_config, 'player_detail', all_player_detail)
    setattr(game_config, 'player_detail_starlevel', starlevel_data)
    setattr(game_config, 'player_detail_starplus', starplus_data)
    setattr(game_config, 'player_detail_material_sort', material_sort_data)

def player_evolution_result_func(game_config, config_name, config_value):
    data = {}
    for _, obj in config_value.iteritems():
        data[obj['starlevel']] = obj
    setattr(game_config, 'player_evolution_starlevel', data)

def award_retire_func(game_config, config_name, config_value):
    needpoint = []
    award_ids = []
    for cfg_id, obj in sorted(config_value.iteritems(), key=lambda x: x[1]['needpoint']):
        needpoint.append(obj['needpoint'])
        award_ids.append(cfg_id)
    setattr(game_config, 'award_retire_sort', {'needpoint': needpoint, 'award_ids': award_ids})

def strategy_func(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        temp = data.setdefault(obj['samestrategy'], {})
        temp[obj['level']] = cfg_id
    setattr(game_config, 'strategy_upgrade', data)

def strategy_emblem_func(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data.setdefault(obj['samestrategy'], []).append(cfg_id)
    for _, value in data.iteritems():
        value.sort()
    setattr(game_config, 'strategy_emblem_samestrategy', data)

def gameshotjudge_func(game_config, config_name, config_value):
    data = {}
    for judge_id, obj in config_value.iteritems():
        temp = data.setdefault(obj['atk_sort'], {})
        temp[obj['comparison_sort']] = judge_id
    setattr(game_config, 'gameshotjudge_sort', data)

def gamestamina_func(game_config, config_name, config_value):
    bottoms = []
    configs = []
    for cfg_id, obj in config_value.iteritems():
        bottoms.append(obj['bottom'])
        configs.append(cfg_id)
    gamestamina_sort = {
        'bottoms': sorted(bottoms),
        'configs': sorted(configs, key=lambda x: config_value[x]['bottom'])
    }
    setattr(game_config, '%s_sort' % config_name, gamestamina_sort)

def skill_active_func(game_config, config_name, config_value):
    upgrades = {}
    effect_sorts = set()
    for cfg_id, obj in config_value.iteritems():
        temp = upgrades.setdefault(obj['sameskill'], {})
        temp[obj['level']] = cfg_id
        effect_sorts.add(obj['effect_sort'])
    setattr(game_config, 'skill_active_upgrade', upgrades)
    setattr(game_config, 'skill_active_effect_sort', effect_sorts)

def skill_passive_func(game_config, config_name, config_value):
    lottery = {}
    lotterylevel = {}
    lottery_sort = {}
    for cfg_id, obj in config_value.iteritems():
        lottery[cfg_id] = obj['weight']
        lotterylevel.setdefault(obj['lotterylevel'], []).append(cfg_id)
        lottery_sort.setdefault(obj['effect_sort'], []).append(cfg_id)
    setattr(game_config, 'skill_passive_lottery', lottery)
    setattr(game_config, 'skill_passive_lotterylevel', sorted(lotterylevel.iteritems()))
    setattr(game_config, 'skill_passive_lottery_sort', lottery_sort)

def pve_chapter_func(game_config, config_name, config_value):
    chatper_sorted = config_value.keys()
    chatper_sorted.sort(key=lambda x: config_value[x]['chapter_order'])
    setattr(game_config, 'pve_chapter_sorted', chatper_sorted)

def pve_stage_func(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data.setdefault(obj['chapter_ID'], []).append(cfg_id)
    for stage_list in data.itervalues():
        stage_list.sort(key=lambda x: config_value[x]['stage_order'], reverse=False)
    setattr(game_config, 'pve_chapter_stage', data)

def pve_blockdetail_func(game_config, config_name, config_value):
    all_blockdetail = getattr(game_config, 'pve_blockdetail_raw', {})
    all_blockdetail.update(config_value)
    all_stage_blockdetail = {}
    all_stage_block = {}
    # 合后的配置格式处理
    for cfg_id, obj in all_blockdetail.iteritems():
        temp = all_stage_blockdetail.setdefault(obj['stage_ID'], {})
        temp[cfg_id] = obj
        all_stage_block.setdefault(obj['stage_ID'], []).append(cfg_id)
    for block_list in all_stage_block.itervalues():
        block_list.sort(key=lambda x: all_blockdetail[x]['block_order'])
    # 当前配置格式数据
    stage_blockdetail = {}
    for cfg_id, obj in config_value.iteritems():
        temp = stage_blockdetail.setdefault(obj['stage_ID'], {})
        temp[cfg_id] = obj
    setattr(game_config, 'pve_blockdetail_raw', all_blockdetail)
    setattr(game_config, 'pve_blockdetail', all_stage_blockdetail)
    setattr(game_config, 'pve_stage_block', all_stage_block)
    setattr(game_config, config_name, stage_blockdetail)

def pve_ranking_func(game_config, config_name, config_value):
    pve_ranking_sort = {}
    for cfg_id, obj in config_value.iteritems():
        temp = pve_ranking_sort.setdefault(obj['conf'], [])
        temp.append(cfg_id)
    setattr(game_config, 'pve_ranking_sort', pve_ranking_sort)

def award_ranking_func(game_config, config_name, config_value):
    ranks = []
    awards = []
    for award_id, obj in sorted(config_value.iteritems(), key=lambda  x: x[1]['start_rank']):
        ranks.append(obj['start_rank'])
        awards.append(award_id)
    award_ranking_sort = {'ranks': ranks, 'awards': awards}
    setattr(game_config, 'award_ranking_sort', award_ranking_sort)

def item_func(game_config, config_name, config_value):
    item_sort = {}
    for cfg_id, obj in config_value.iteritems():
        item_sort.setdefault(obj['sort'], []).append(cfg_id)
    setattr(game_config, 'item_sort', item_sort)

def robmoney_func(game_config, config_name, config_value):
    lvrange = []
    cfg_ids = []
    for cfg_id, obj in sorted(config_value.iteritems(), key=lambda x: x[1]['rangelvmax']):
        lvrange.append(obj['rangelvmax'])
        cfg_ids.append(cfg_id)
    robmoney_sort = {'lvrange': lvrange, 'cfg_ids': cfg_ids}
    setattr(game_config, 'robmoney_sort', robmoney_sort)

def patch_merge_func(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        for patch_id in obj['patch']:
            data[patch_id] = cfg_id
    setattr(game_config, 'patch_merge_map', data)

def celebration_func(game_config, config_name, config_value):
    celebration_sort = {}
    for cfg_id, obj in config_value.iteritems():
        temp = celebration_sort.setdefault(obj['sort'], [])
        temp.append(cfg_id)
    for sort_list in celebration_sort.itervalues():
        sort_list.sort()
    setattr(game_config, 'celebration_sort', celebration_sort)

def activity_e_func(game_config, config_name, config_value):
    activity_sameact = {}
    for cfg_id, obj in config_value.iteritems():
        temp = activity_sameact.setdefault(obj['sameact'], [])
        temp.append(cfg_id)
    for sameact_list in activity_sameact.itervalues():
        sameact_list.sort()
    setattr(game_config, 'activity_e_sameact', activity_sameact)

def equip_detail_func(game_config, config_name, config_value):
    all_equip_detail = getattr(game_config, 'equip_detail', {})
    all_equip_detail.update(config_value)
    equip_detail_tiername = {}
    star_sort = {}
    samename_star_advanced = {}
    for cfg_id, obj in all_equip_detail.iteritems():
        temp1 = equip_detail_tiername.setdefault(obj['tiername'], {}).setdefault(obj['star'], {})
        temp1[obj['advanced']] = cfg_id

        temp2 = star_sort.setdefault(obj['star'], {})
        temp2[obj['sort']] = cfg_id

        temp3 = samename_star_advanced.setdefault(obj['samename'], {}).setdefault(obj['star'], {})
        temp3[obj['advanced']] = cfg_id

    setattr(game_config, 'equip_detail', all_equip_detail)
    setattr(game_config, 'equip_detail_tiername', equip_detail_tiername)
    setattr(game_config, 'equip_detail_star_sort', star_sort)
    setattr(game_config, 'equip_detail_samename_star_advanced', samename_star_advanced)

def equip_mix_func(game_config, config_name, config_value):
    data = {}
    for _, obj in config_value.iteritems():
        temp = data.setdefault(obj['star'], {})
        temp[obj['mix_sort']] = obj
    setattr(game_config, config_name, data)

def award_arena_func(game_config, config_name, config_value):
    ranks = []
    awards = []
    for award_id, obj in sorted(config_value.iteritems(), key=lambda  x: x[1]['start_rank']):
        ranks.append(obj['start_rank'])
        awards.append(award_id)
    award_arena_sort = {'ranks': ranks, 'awards': awards}
    setattr(game_config, 'award_arena_sort', award_arena_sort)

def goods_diamond_func(game_config, config_name, config_value):
    goods_diamond_sort = {}
    for cfg_id, obj in config_value.iteritems():
        temp = goods_diamond_sort.setdefault(obj['section'], [])
        temp.append(cfg_id)
    for section in goods_diamond_sort:
        goods_diamond_sort[section].sort(key=lambda x: config_value[x]['order'])
    setattr(game_config, 'goods_diamond_sort', goods_diamond_sort)

def guide_func(game_config, config_name, config_value):
    guidegroup = {}
    sectiongroup = {}
    for cfg_id, obj in config_value.iteritems():
        temp = guidegroup.setdefault(obj['guidegroup'], {})
        temp[cfg_id] = obj
        temp2 = sectiongroup.setdefault(obj['sectiongroup'], [])
        temp2.append(cfg_id)
    setattr(game_config, 'guide_raw', config_value)
    setattr(game_config, 'guide_sectiongroup', sectiongroup)
    setattr(game_config, config_name, guidegroup)

def guideformation_func(game_config, config_name, config_value):
    formation_team = {}
    for cfg_id, obj in config_value.iteritems():
        formation_team.setdefault(obj['team'], []).append(cfg_id)
    for _, pos_list in formation_team.iteritems():
        pos_list.sort(key=lambda x: config_value[x]['pos'])
    setattr(game_config, 'guideformation_sort', formation_team)

def award_task_func(game_config, config_name, config_value):
    award_task_sort = {}
    award_task_section = {}
    for cfg_id, obj in config_value.iteritems():
        award_task_sort.setdefault(obj['type'], []).append(cfg_id)
        award_task_section.setdefault(obj['section'], []).append(cfg_id)
    for _, task_list in award_task_section.iteritems():
        task_list.sort(key=lambda x: config_value[x]['order'])
    setattr(game_config, 'award_task_sort', award_task_sort)
    setattr(game_config, 'award_task_section', award_task_section)

def gacha_box_func(game_config, config_name, config_value):
    gacha_box_key = {}
    for cfg_id, obj in config_value.iteritems():
        gacha_box_key[obj['key']] = cfg_id
    setattr(game_config, 'gacha_box_key', gacha_box_key)

def pve_moneystage_func(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data.setdefault(obj['chapter_ID'], []).append(cfg_id)
    for stage_list in data.itervalues():
        stage_list.sort()
    chapter_order = sorted(data, key=lambda x: config_value[data[x][0]]['chapter_order'])
    setattr(game_config, 'pve_moneychapter_order', chapter_order)
    setattr(game_config, 'pve_moneychapter_moneystage', data)

def loot_server_func(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        if obj['is_gacha'] == 1:
            data[cfg_id] = obj
    setattr(game_config, 'loot_server_gacha', data)

def pvp_sectionvs_func(game_config, config_name, config_value):
    data = {}
    pvp_sectionvs_order = []
    for cfg_id, obj in config_value.iteritems():
        data.setdefault(obj['is_solo'], []).append(cfg_id)
        pvp_sectionvs_order.append(cfg_id)
    for stage_list in data.itervalues():
        stage_list.sort(key=lambda x:config_value[x]['order'])
    pvp_sectionvs_order.sort(key=lambda x:config_value[x]['order'])
    setattr(game_config, 'pvp_sectionvs_solo', data)
    setattr(game_config, 'pvp_sectionvs_order', pvp_sectionvs_order)

def award_vsrankseason_func(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data.setdefault(obj['section_vs'], []).append(cfg_id)
    setattr(game_config, 'award_vsrankseason_section', data)

def award_vsrankwin_func(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data.setdefault(obj['section_vs'], []).append(cfg_id)
    setattr(game_config, 'award_vsrankwin_section', data)

def award_vsturnloot_func(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data.setdefault(obj['section'], []).append(cfg_id)
    setattr(game_config, 'award_vsturnloot_section', data)

def award_signday2_func(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data.setdefault(obj['round'], []).append(cfg_id)
    for days_list in data.itervalues():
        days_list.sort()
    setattr(game_config, 'award_signday2_round', data)

def activity_diamond_func(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        temp = data.setdefault(obj['same_arm'], {})
        temp[obj['time']] = cfg_id
    setattr(game_config, 'activity_diamond_same_arm', data)

def pve_hstage_func(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data.setdefault(obj['chapter_ID'], []).append(cfg_id)
    for stage_list in data.itervalues():
        stage_list.sort(key=lambda x: config_value[x]['stage_order'], reverse=False)
    setattr(game_config, 'pve_hchapter_hstage', data)


def player_tutor_func(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data.setdefault(obj['sametutor'], []).append(cfg_id)
    for starlevel_list in data.itervalues():
        starlevel_list.sort(key=lambda x: config_value[x]['starlevel'])

    setattr(game_config, 'player_tutor_sametutor', data)


def item_merge_func(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data[obj['object_item']] = cfg_id
    setattr(game_config, 'item_merge_object_item', data)


def activity_roulettefresh_func(game_config, config_name, config_value):
    same_roulette = {}
    show_sort = {}
    for cfg_id, obj in config_value.iteritems():
        same_roulette.setdefault(obj['same_roulette'], []).append(cfg_id)
        show_sort.setdefault(obj['show_sort'], []).append(cfg_id)
    for days_list in same_roulette.itervalues():
        days_list.sort()
    for days_list in show_sort.itervalues():
        days_list.sort()
    setattr(game_config, 'activity_roulettefresh_same_roulette', same_roulette)
    setattr(game_config, 'activity_roulettefresh_show_sort', show_sort)

def activity_roulette_func(game_config, config_name, config_value):
    gacha_sort = {}
    for cfg_id, obj in config_value.iteritems():
        gacha_sort.setdefault(obj['gacha_sort'], []).append(cfg_id)
    setattr(game_config, 'activity_roulette_gacha_sort', gacha_sort)

def text_getshow_func(game_config, config_name, config_value):
    detail_list = []
    for cfg_id, obj in config_value.iteritems():
        if obj['detail']:
            detail_list.append(obj['detail'])
    setattr(game_config, 'text_getshow_detail_list', detail_list)

def goods_roulette_func(game_config, config_name, config_value):
    same_goodsroulette = {}
    for cfg_id, obj in config_value.iteritems():
        same_goodsroulette.setdefault(obj['same_goodsroulette'], []).append(cfg_id)
    for id_list in same_goodsroulette.itervalues():
        id_list.sort(key=lambda x: config_value[x]['order'])
    setattr(game_config, 'goods_roulette_same_goodsroulette', same_goodsroulette)


def loot_double_func(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data.setdefault(obj['object_sort'], []).append(cfg_id)
    setattr(game_config, 'loot_double_object_sort', data)


def loot_func(game_config, config_name, config_value):
    all_loot = getattr(game_config, 'loot', {})
    all_loot.update(config_value)

    setattr(game_config, 'loot', all_loot)


config_name_list = (
    # (config_key,     config_sub_func, is_show_in_admin, is_modifable, xsl_table_name, send_to_client
    ('resource_versions', ()                  , 0, 0, None              , 0),
    ('resource_update' , ()                   , 0, 0, None              , 0),
    ('servers'         , (servers_func,)      , 0, 0, None              , 0),
    ('system_notify'   , ()                   , 0, 0, None              , 0),
    ('award_sp'        , ()                   , 1, 1, 'award_sp'        , 0),
    ('award_sp2'       , ()                   , 1, 1, 'award_sp2'       , 0),
    ('award_sp3'       , ()                   , 1, 1, 'award_sp3'       , 0),
    ('award_sp4'       , ()                   , 1, 1, 'award_sp4'       , 0),
    ('serverctrl'      , ()                   , 1, 1, 'serverctrl'      , 0),
    ('text_warning'    , ()                   , 1, 1, 'text_warning'    , 0),
    ('text_hexie'      , ()                   , 1, 1, 'text_hexie'      , 0),
    ('celebration'     , (celebration_func,)  , 1, 1, 'celebration'     , 1),
    ('activity_e'      , (activity_e_func,)   , 1, 1, 'activity_e'      , 1),
    ('charge'          , (charge_func,)       , 1, 1, 'charge'          , 0),
    ('week_gift'       , ()                   , 1, 1, 'week_gift'       , 1),
    ('month_gift'      , ()                   , 1, 1, 'month_gift'      , 1),
    ('user_info'       , (user_info_func,)    , 1, 1, 'user_info'       , 0),
    ('user_select'     , ()                   , 1, 1, 'user_select'     , 1),
    ('user_functrl'    , ()                   , 1, 1, 'user_functrl'    , 1),
    ('user_ini'        , ()                   , 1, 1, 'user_ini'        , 1),
    ('goods_arena'     , ()                   , 1, 1, 'goods_arena'     , 1),
    ('goods_diamond'   , (goods_diamond_func,), 1, 1, 'goods_diamond'   , 1),
    ('goods_code'      , ()                   , 1, 1, 'goods_code'      , 0),
    ('goods_deadrefresh',()                   , 1, 1, 'goods_deadrefresh',0),
    ('goods_deaddetail' ,()                   , 1, 1, 'goods_deaddetail', 1),
    ('goods_dynastydetail' , ()               , 1, 1, 'goods_dynastydetail' , 1),
    ('goods_dynastyrefresh', ()               , 1, 1, 'goods_dynastyrefresh', 0),
    ('goods_money'     , ()                   , 1, 1, 'goods_money'      , 1),
    ('goods_leaguedetail'   , ()              , 1, 1, 'goods_leaguedetail'  , 1),
    ('goods_leaguefresh'    , ()              , 1, 1, 'goods_leaguefresh'   , 0),
    ('player_detail1a' , (player_detail_func,), 1, 1, 'player_detail1A'  , 1),
    ('player_detail1b' , (player_detail_func,), 1, 1, 'player_detail1B'  , 1),
    ('player_detail1c' , (player_detail_func,), 1, 1, 'player_detail1C'  , 1),
    ('player_detail2a' , (player_detail_func,), 1, 1, 'player_detail2A'  , 1),
    ('player_detail2b' , (player_detail_func,), 1, 1, 'player_detail2B'  , 1),
    ('player_detail3a' , (player_detail_func,), 1, 1, 'player_detail3A'  , 1),
    ('player_detail3b' , (player_detail_func,), 1, 1, 'player_detail3B'  , 1),
    ('player_detail4a' , (player_detail_func,), 1, 1, 'player_detail4A'  , 1),
    ('player_detail4b' , (player_detail_func,), 1, 1, 'player_detail4B'  , 1),
    ('player_detail5'  , (player_detail_func,), 1, 1, 'player_detail5'   , 1),
    ('player_detail6a' , (player_detail_func,), 1, 1, 'player_detail6A'  , 1),
    ('player_detail6b' , (player_detail_func,), 1, 1, 'player_detail6B'  , 1),
    ('player_evolution_result', (player_evolution_result_func,)   , 1, 1, 'player_evolution_result' , 1),
    ('player_book'     , ()                   , 1, 1, 'player_book'     , 1),
    ('player_exp'      , ()                   , 1, 1, 'player_exp'      , 1),
    ('player_retire'   , ()                   , 1, 1, 'player_retire'   , 1),
    ('player_rebirth_exp'     , ()            , 1, 1, 'player_rebirth_exp'      , 0),
    ('player_rebirth_material', ()            , 1, 1, 'player_rebirth_material' , 1),
    ('player_mix'      , ()                   , 1, 1, 'player_mix'      , 1),
    ('player_mixnum'   , ()                   , 1, 1, 'player_mixnum'   , 0),
    ('player_sameevo'  , ()                   , 1, 1, 'player_sameevo'  , 1),
    ('equip_detail1'   , (equip_detail_func,) , 1, 1, 'equip_detail1'   , 1),
    ('equip_detail2'   , (equip_detail_func,) , 1, 1, 'equip_detail2'   , 1),
    ('equip_detail3'   , (equip_detail_func,) , 1, 1, 'equip_detail3'   , 1),
    ('equip_detail4'   , (equip_detail_func,) , 1, 1, 'equip_detail4'   , 1),
    ('equip_detail5'   , (equip_detail_func,) , 1, 1, 'equip_detail5'   , 1),
    ('equip_detail6'   , (equip_detail_func,) , 1, 1, 'equip_detail6'   , 1),
    ('equip_type'      , ()                   , 1, 1, 'equip_type'      , 1),
    ('equip_retire'    , ()                   , 1, 1, 'equip_retire'    , 1),
    ('equip_tier'      , ()                   , 1, 1, 'equip_tier'      , 1),
    #('equip_rebirth_exp'     , ()             , 1, 1, 'equip_rebirth_exp'     , 0),
    ('equip_rebirth_material', ()             , 1, 1, 'equip_rebirth_material', 1),
    ('equip_mix'       , (equip_mix_func,)    , 1, 1, 'equip_mix'       , 1),
    ('equip_mixnum'    , ()                   , 1, 1, 'equip_mixnum'    , 0),
    ('gameshotlevel'   , ()                   , 1, 1, 'gameshotlevel'   , 1),
    ('gameshotjudge'   , (gameshotjudge_func,), 1, 1, 'gameshotjudge'   , 1),
    ('gameastcount'    , ()                   , 1, 1, 'gameastcount'    , 1),
    ('gameshotcount'   , ()                   , 1, 1, 'gameshotcount'   , 1),
    ('gameragejudge'   , ()                   , 1, 1, 'gameragejudge'   , 1),
    ('gamedefence'     , ()                   , 1, 1, 'gamedefence'     , 1),
    ('gamestamina_new' , (gamestamina_func,)  , 1, 1, 'gamestamina_new' , 1),
    ('gamestamina_strike', ()                 , 1, 1, 'gamestamina_strike', 1),
    ('gametime_new'    , ()                   , 1, 1, 'gametime_new'    , 1),
    ('gamereporter'    , ()                   , 1, 1, 'gamereporter'    , 1),
    ('gameeventlibrary', ()                   , 1, 1, 'gameeventlibrary', 1),
    ('gamesuperskill'  , ()                   , 1, 1, 'gamesuperskill'  , 1),
    ('gamecounter'     , ()                   , 1, 1, 'gamecounter'     , 1),
    ('strategy'        , (strategy_func,)     , 1, 1, 'strategy'        , 1),
    ('strategy_emblem' , (strategy_emblem_func,), 1, 1, 'strategy_emblem' , 1),
    ('skill_active'    , (skill_active_func,) , 1, 1, 'skill_active'    , 1),
    ('skill_passive'   , (skill_passive_func,), 1, 1, 'skill_passive'   , 1),
    ('skill_passivetrain', ()                 , 1, 1, 'skill_passivetrain', 1),
    ('skill_jointly'   , ()                   , 1, 1, 'skill_jointly'   , 1),
    ('pve_chapter'     , (pve_chapter_func,)  , 1, 1, 'PvE_chapter'     , 1),
    ('pve_stage'       , (pve_stage_func,)    , 1, 1, 'PvE_stage'       , 1),
    ('pve_blockdetail1', (pve_blockdetail_func,), 1, 1, 'PvE_blockdetail1', 1),
    ('pve_blockdetail2', (pve_blockdetail_func,), 1, 1, 'PvE_blockdetail2', 1),
    ('pve_blockdetail3', (pve_blockdetail_func,), 1, 1, 'PvE_blockdetail3', 1),
    ('pve_blockdetail4', (pve_blockdetail_func,), 1, 1, 'PvE_blockdetail4', 1),
    ('pve_blockdetail5', (pve_blockdetail_func,), 1, 1, 'PvE_blockdetail5', 1),
    ('pve_blockdetail6', (pve_blockdetail_func,), 1, 1, 'PvE_blockdetail6', 1),
    ('pve_gamedetail'  , ()                   , 1, 1, 'PvE_gamedetail'  , 1),
    ('pve_friendbuff'  , ()                   , 1, 1, 'PvE_friendbuff'  , 0),
    ('pve_game1v1'     , ()                   , 1, 1, 'PvE_game1v1'     , 1),
    ('pve_ranking'     , (pve_ranking_func,)  , 1, 1, 'PvE_ranking'     , 0),
    ('pvp_gamearena'   , ()                   , 1, 1, 'PvP_gamearena'   , 0),
    ('pve_dice'        , ()                   , 1, 1, 'PvE_dice'        , 0),
    ('pve_dicenew'     , ()                   , 1, 1, 'PvE_dicenew'     , 0),
    ('pve_legendchapter', ()                  , 1, 1, 'PvE_legendchapter', 1),
    ('pve_dynastydetail', ()                  , 1, 1, 'PvE_dynastydetail', 1),
    ('pve_moneystage' , (pve_moneystage_func,), 1, 1, 'PvE_moneystage'   , 1),
    ('monster_arena'   , ()                   , 1, 1, 'monster_arena'   , 1),
    ('monster_vs'      , ()                   , 1, 1, 'monster_vs'      , 1),
    ('monster_robpatch', ()                   , 1, 1, 'monster_robpatch', 1),
    ('monster_op'      , ()                   , 1, 1, 'monster_op'      , 1),
    ('monster_money'   , ()                   , 1, 1, 'monster_money'   , 1),
    ('monster_system'  , ()                   , 1, 1, 'monster_system'  , 1),
    ('monster_main'    , ()                   , 1, 1, 'monster_main'    , 1),
    ('monster_main11'  , ()                   , 1, 1, 'monster_main11'  , 1),
    ('monster_main21'  , ()                   , 1, 1, 'monster_main21'  , 1),
    ('monster_main31'  , ()                   , 1, 1, 'monster_main31'  , 1),
    ('monster_1v1'     , ()                   , 1, 1, 'monster_1v1'     , 1),
    ('monster_dynasty' , ()                   , 1, 1, 'monster_dynasty' , 1),
    ('monster_legend'  , ()                   , 1, 1, 'monster_legend'  , 1),
    ('loot0'           , (loot_func,)         , 1, 1, 'loot'            , 0),
    ('loot1'           , (loot_func,)         , 1, 1, 'loot1'           , 0),
    ('loot_server'     , (loot_server_func,)  , 1, 1, 'loot_server'     , 0),
    ('text'            , ()                   , 1, 1, 'text'            , 1),
    ('item'            , (item_func,)         , 1, 1, 'item'            , 1),
    ('logo'            , ()                   , 1, 1, 'logo'            , 1),
    ('conf'            , ()                   , 1, 1, 'conf'            , 1),
    ('zone'            , ()                   , 1, 1, 'zone'            , 1),
    ('robmoney'        , (robmoney_func,)     , 1, 1, 'robmoney'        , 1),
    ('robpatch'        , ()                   , 1, 1, 'robpatch'        , 1),
    ('robplayer'       , ()                   , 1, 1, 'robplayer'       , 1),
    ('patch_merge'     , (patch_merge_func,)  , 1, 1, 'patch_merge'     , 1),
    ('resource'        , ()                   , 1, 1, 'resource'        , 1),
    ('cost_diamond'    , ()                   , 1, 1, 'cost_diamond'    , 1),
    ('celebration_yao' , ()                   , 1, 1, 'celebration_yao' , 0),
    ('floor_detail'    , ()                   , 1, 1, 'floor_detail'    , 1),
    ('vip_function'    , ()                   , 1, 1, 'vip_function'    , 1),
    ('random_name'     , ()                   , 1, 1, 'random_name'     , 0),
    ('bulletin'        , ()                   , 1, 1, 'bulletin'        , 0),
    ('gonglve'         , ()                   , 1, 1, 'gonglve'         , 1),
    ('treasure'        , ()                   , 1, 1, 'treasure'        , 1),
    ('gacha_box'        ,(gacha_box_func,)    , 1, 1, 'gacha_box'       , 1),
    ('gacha'           , ()                   , 1, 1, 'gacha'           , 1),
    ('gacha_equip'     , ()                   , 1, 1, 'gacha_equip'     , 1),
    ('patchplayer'     , ()                   , 1, 1, 'patchplayer'     , 1),
    ('patchequip'      , ()                   , 1, 1, 'patchequip'      , 1),
    ('guide'           , (guide_func,)        , 1, 1, 'guide'           , 1),
    ('guidestreet'     , ()                   , 1, 1, 'guidestreet'     , 1),
    ('guidebattle'     , ()                   , 1, 1, 'guidebattle'     , 1),
    ('guidebattleini'  , ()                   , 1, 1, 'guidebattleini'  , 1),
    ('guideformation'  , (guideformation_func,), 1, 1, 'guideformation' , 1),
    ('text_home'       , ()                   , 1, 1, 'text_home'       , 1),
    ('award_ranking'   , (award_ranking_func,), 1, 1, 'award_ranking'   , 1),
    ('award_retire'    , (award_retire_func,) , 1, 1, 'award_retire'    , 1),
    ('award_arena'     , (award_arena_func,)  , 1, 1, 'award_arena'     , 1),
    ('award_signday'   , ()                   , 1, 1, 'award_signday'   , 1),
    ('award_signday2'  , (award_signday2_func,), 1, 1, 'award_signday2' , 0),
    ('award_signmon'   , ()                   , 1, 1, 'award_signmon'   , 1),
    ('award_signnew'   , ()                   , 1, 1, 'award_signnew'   , 1),
    ('award_level'     , ()                   , 1, 1, 'award_level'     , 1),
    ('award_task'      , (award_task_func,)   , 1, 1, 'award_task'      , 1),
    ('award_dau'       , ()                   , 1, 1, 'award_DAU'       , 0),
    ('formation_backup', ()                   , 1, 1, 'formation_backup', 1),
    ('pvp_gamepatch'   , ()                   , 1, 1, 'PvP_gamepatch'   , 0),
    ('systemfriend'    , ()                   , 1, 1, 'systemfriend'    , 0),
    ('league_build'    , ()                   , 1, 1, 'league_build'    , 1),
    ('league_info'     , ()                   , 1, 1, 'league_info'     , 0),
    ('league_worship'  , ()                   , 1, 1, 'league_worship'  , 1),
    ('league_donate'   , ()                   , 1, 1, 'league_donate'   , 1),
    ('pvp_ranking'     , ()                   , 1, 1, 'pvp_ranking'     , 1),
    ('pvp_sectionvs'   , (pvp_sectionvs_func,), 1, 1, 'PvP_sectionvs'   , 1),
    ('pvp_gamevs'      , ()                   , 1, 1, 'PvP_gamevs'      , 0),
    ('pvp_kvs'         , ()                   , 1, 1, 'PvP_Kvs'         , 0),
    ('award_vsrankseason', (award_vsrankseason_func,), 1, 1, 'award_vsrankseason', 0),
    ('award_vsrankwin' , (award_vsrankwin_func,), 1, 1, 'award_vsrankwin' , 0),
    ('award_vsturnloot', (award_vsturnloot_func,),1, 1, 'award_vsturnloot', 0),
    ('random_namevs'   , ()                   , 1, 1, 'random_namevs'   , 0),
    ('goods_vs'        , ()                   , 1, 1, 'goods_vs'        , 1),
    ('pvp_gamevs2'     , ()                   , 1, 1, 'PvP_gamevs2'     , 0),
    ('activity_diamond', (activity_diamond_func,), 1, 1, 'activity_diamond', 0),
    ('pve_hchapter'    , ()                   , 1, 1, 'PvE_Hchapter'    , 1),
    ('pve_hstage'      , (pve_hstage_func,)   , 1, 1, 'PvE_Hstage'      , 1),
    ('player_tutor'    , (player_tutor_func,) , 1, 1, 'player_tutor'    , 1),
    ('item_merge'      , (item_merge_func,)   , 1, 1, 'item_merge'      , 1),
    ('patchitem'       , ()                   , 1, 1, 'patchitem'       , 1),
    ('activity_roulettefresh', (activity_roulettefresh_func,), 1, 1, 'activity_roulettefresh', 0),
    ('activity_roulette', (activity_roulette_func,), 1, 1, 'activity_roulette', 0),
    ('goods_roulette'   , (goods_roulette_func,)   , 1, 1, 'goods_roulette'   , 0),
    ('text_getshow'     , (text_getshow_func,)     , 1, 1, 'text_getshow'     , 1),
    ('award_fund'       , ()                   , 1, 1, 'award_fund'      , 1),
    ('award_arenafirst' , ()                   , 1, 1, 'award_arenafirst'     , 0),
    ('type_diamond'     , ()                   , 1, 1, 'type_diamond'    , 0),
    ('loot_double'      , (loot_double_func,)  , 1, 1, 'loot_double'     , 0),
)


