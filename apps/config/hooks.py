# coding: utf-8


def servers_f(game_config, config_name, config_value):
    pass
#     import settings
#     for server_id, obj in config_value.iteritems():
#         settings.SERVERS[server_id] = {'db_index': obj.get('db_index', 0),
#                                        'db_key': obj.get('db_key', '')}
#     # 设定默认的分服db设置
#     if '00' not in settings.SERVERS:
#         settings.SERVERS['00'] = {'db_index': 0, 'db_key': ''}


def charge_f(game_config, config_name, config_value):
    """充值定单配置，额外增加商品id到配置的映射配置
    """
    data = {}
    open_gifts = {}
    for buy_id, obj in config_value.iteritems():
        data[obj['cost']] = buy_id
        open_gifts.setdefault(obj['open_gift'], []).append(buy_id)
    setattr(game_config, 'charge_scheme', data)
    setattr(game_config, 'charge_open_gift', open_gifts)


def user_info_f(game_config, config_name, config_value):
    rent_num_openlv = {}
    for level, obj in sorted(config_value.iteritems()):
        if obj['rent_num'] not in rent_num_openlv:
            rent_num_openlv[obj['rent_num']] = level
    setattr(game_config, 'rent_num_openlv', rent_num_openlv)


def player_detail_f(game_config, config_name, config_value):
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


def player_evolution_result_f(game_config, config_name, config_value):
    data = {}
    for _, obj in config_value.iteritems():
        data[obj['starlevel']] = obj
    setattr(game_config, 'player_evolution_starlevel', data)


def award_retire_f(game_config, config_name, config_value):
    needpoint = []
    award_ids = []
    for cfg_id, obj in sorted(config_value.iteritems(), key=lambda x: x[1]['needpoint']):
        needpoint.append(obj['needpoint'])
        award_ids.append(cfg_id)
    setattr(game_config, 'award_retire_sort', {'needpoint': needpoint, 'award_ids': award_ids})

def strategy_f(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        temp = data.setdefault(obj['samestrategy'], {})
        temp[obj['level']] = cfg_id
    setattr(game_config, 'strategy_upgrade', data)

def strategy_emblem_f(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data.setdefault(obj['samestrategy'], []).append(cfg_id)
    for _, value in data.iteritems():
        value.sort()
    setattr(game_config, 'strategy_emblem_samestrategy', data)

def gameshotjudge_f(game_config, config_name, config_value):
    data = {}
    for judge_id, obj in config_value.iteritems():
        temp = data.setdefault(obj['atk_sort'], {})
        temp[obj['comparison_sort']] = judge_id
    setattr(game_config, 'gameshotjudge_sort', data)

def gamestamina_f(game_config, config_name, config_value):
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

def skill_active_f(game_config, config_name, config_value):
    upgrades = {}
    effect_sorts = set()
    for cfg_id, obj in config_value.iteritems():
        temp = upgrades.setdefault(obj['sameskill'], {})
        temp[obj['level']] = cfg_id
        effect_sorts.add(obj['effect_sort'])
    setattr(game_config, 'skill_active_upgrade', upgrades)
    setattr(game_config, 'skill_active_effect_sort', effect_sorts)

def skill_passive_f(game_config, config_name, config_value):
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

def pve_chapter_f(game_config, config_name, config_value):
    chatper_sorted = config_value.keys()
    chatper_sorted.sort(key=lambda x: config_value[x]['chapter_order'])
    setattr(game_config, 'pve_chapter_sorted', chatper_sorted)

def pve_stage_f(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data.setdefault(obj['chapter_ID'], []).append(cfg_id)
    for stage_list in data.itervalues():
        stage_list.sort(key=lambda x: config_value[x]['stage_order'], reverse=False)
    setattr(game_config, 'pve_chapter_stage', data)

def pve_blockdetail_f(game_config, config_name, config_value):
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

def pve_ranking_f(game_config, config_name, config_value):
    pve_ranking_sort = {}
    for cfg_id, obj in config_value.iteritems():
        temp = pve_ranking_sort.setdefault(obj['conf'], [])
        temp.append(cfg_id)
    setattr(game_config, 'pve_ranking_sort', pve_ranking_sort)

def award_ranking_f(game_config, config_name, config_value):
    ranks = []
    awards = []
    for award_id, obj in sorted(config_value.iteritems(), key=lambda  x: x[1]['start_rank']):
        ranks.append(obj['start_rank'])
        awards.append(award_id)
    award_ranking_sort = {'ranks': ranks, 'awards': awards}
    setattr(game_config, 'award_ranking_sort', award_ranking_sort)

def item_f(game_config, config_name, config_value):
    item_sort = {}
    for cfg_id, obj in config_value.iteritems():
        item_sort.setdefault(obj['sort'], []).append(cfg_id)
    setattr(game_config, 'item_sort', item_sort)

def robmoney_f(game_config, config_name, config_value):
    lvrange = []
    cfg_ids = []
    for cfg_id, obj in sorted(config_value.iteritems(), key=lambda x: x[1]['rangelvmax']):
        lvrange.append(obj['rangelvmax'])
        cfg_ids.append(cfg_id)
    robmoney_sort = {'lvrange': lvrange, 'cfg_ids': cfg_ids}
    setattr(game_config, 'robmoney_sort', robmoney_sort)

def patch_merge_f(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        for patch_id in obj['patch']:
            data[patch_id] = cfg_id
    setattr(game_config, 'patch_merge_map', data)

def celebration_f(game_config, config_name, config_value):
    celebration_sort = {}
    for cfg_id, obj in config_value.iteritems():
        temp = celebration_sort.setdefault(obj['sort'], [])
        temp.append(cfg_id)
    for sort_list in celebration_sort.itervalues():
        sort_list.sort()
    setattr(game_config, 'celebration_sort', celebration_sort)

def activity_e_f(game_config, config_name, config_value):
    activity_sameact = {}
    for cfg_id, obj in config_value.iteritems():
        temp = activity_sameact.setdefault(obj['sameact'], [])
        temp.append(cfg_id)
    for sameact_list in activity_sameact.itervalues():
        sameact_list.sort()
    setattr(game_config, 'activity_e_sameact', activity_sameact)

def equip_detail_f(game_config, config_name, config_value):
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

def equip_mix_f(game_config, config_name, config_value):
    data = {}
    for _, obj in config_value.iteritems():
        temp = data.setdefault(obj['star'], {})
        temp[obj['mix_sort']] = obj
    setattr(game_config, config_name, data)

def award_arena_f(game_config, config_name, config_value):
    ranks = []
    awards = []
    for award_id, obj in sorted(config_value.iteritems(), key=lambda  x: x[1]['start_rank']):
        ranks.append(obj['start_rank'])
        awards.append(award_id)
    award_arena_sort = {'ranks': ranks, 'awards': awards}
    setattr(game_config, 'award_arena_sort', award_arena_sort)

def goods_diamond_f(game_config, config_name, config_value):
    goods_diamond_sort = {}
    for cfg_id, obj in config_value.iteritems():
        temp = goods_diamond_sort.setdefault(obj['section'], [])
        temp.append(cfg_id)
    for section in goods_diamond_sort:
        goods_diamond_sort[section].sort(key=lambda x: config_value[x]['order'])
    setattr(game_config, 'goods_diamond_sort', goods_diamond_sort)

def guide_f(game_config, config_name, config_value):
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

def guideformation_f(game_config, config_name, config_value):
    formation_team = {}
    for cfg_id, obj in config_value.iteritems():
        formation_team.setdefault(obj['team'], []).append(cfg_id)
    for _, pos_list in formation_team.iteritems():
        pos_list.sort(key=lambda x: config_value[x]['pos'])
    setattr(game_config, 'guideformation_sort', formation_team)

def award_task_f(game_config, config_name, config_value):
    award_task_sort = {}
    award_task_section = {}
    for cfg_id, obj in config_value.iteritems():
        award_task_sort.setdefault(obj['type'], []).append(cfg_id)
        award_task_section.setdefault(obj['section'], []).append(cfg_id)
    for _, task_list in award_task_section.iteritems():
        task_list.sort(key=lambda x: config_value[x]['order'])
    setattr(game_config, 'award_task_sort', award_task_sort)
    setattr(game_config, 'award_task_section', award_task_section)

def gacha_box_f(game_config, config_name, config_value):
    gacha_box_key = {}
    for cfg_id, obj in config_value.iteritems():
        gacha_box_key[obj['key']] = cfg_id
    setattr(game_config, 'gacha_box_key', gacha_box_key)

def pve_moneystage_f(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data.setdefault(obj['chapter_ID'], []).append(cfg_id)
    for stage_list in data.itervalues():
        stage_list.sort()
    chapter_order = sorted(data, key=lambda x: config_value[data[x][0]]['chapter_order'])
    setattr(game_config, 'pve_moneychapter_order', chapter_order)
    setattr(game_config, 'pve_moneychapter_moneystage', data)

def loot_server_f(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        if obj['is_gacha'] == 1:
            data[cfg_id] = obj
    setattr(game_config, 'loot_server_gacha', data)

def pvp_sectionvs_f(game_config, config_name, config_value):
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

def award_vsrankseason_f(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data.setdefault(obj['section_vs'], []).append(cfg_id)
    setattr(game_config, 'award_vsrankseason_section', data)

def award_vsrankwin_f(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data.setdefault(obj['section_vs'], []).append(cfg_id)
    setattr(game_config, 'award_vsrankwin_section', data)

def award_vsturnloot_f(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data.setdefault(obj['section'], []).append(cfg_id)
    setattr(game_config, 'award_vsturnloot_section', data)

def award_signday2_f(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data.setdefault(obj['round'], []).append(cfg_id)
    for days_list in data.itervalues():
        days_list.sort()
    setattr(game_config, 'award_signday2_round', data)

def activity_diamond_f(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        temp = data.setdefault(obj['same_arm'], {})
        temp[obj['time']] = cfg_id
    setattr(game_config, 'activity_diamond_same_arm', data)

def pve_hstage_f(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data.setdefault(obj['chapter_ID'], []).append(cfg_id)
    for stage_list in data.itervalues():
        stage_list.sort(key=lambda x: config_value[x]['stage_order'], reverse=False)
    setattr(game_config, 'pve_hchapter_hstage', data)


def player_tutor_f(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data.setdefault(obj['sametutor'], []).append(cfg_id)
    for starlevel_list in data.itervalues():
        starlevel_list.sort(key=lambda x: config_value[x]['starlevel'])

    setattr(game_config, 'player_tutor_sametutor', data)


def item_merge_f(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data[obj['object_item']] = cfg_id
    setattr(game_config, 'item_merge_object_item', data)


def activity_roulettefresh_f(game_config, config_name, config_value):
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

def activity_roulette_f(game_config, config_name, config_value):
    gacha_sort = {}
    for cfg_id, obj in config_value.iteritems():
        gacha_sort.setdefault(obj['gacha_sort'], []).append(cfg_id)
    setattr(game_config, 'activity_roulette_gacha_sort', gacha_sort)

def text_getshow_f(game_config, config_name, config_value):
    detail_list = []
    for cfg_id, obj in config_value.iteritems():
        if obj['detail']:
            detail_list.append(obj['detail'])
    setattr(game_config, 'text_getshow_detail_list', detail_list)

def goods_roulette_f(game_config, config_name, config_value):
    same_goodsroulette = {}
    for cfg_id, obj in config_value.iteritems():
        same_goodsroulette.setdefault(obj['same_goodsroulette'], []).append(cfg_id)
    for id_list in same_goodsroulette.itervalues():
        id_list.sort(key=lambda x: config_value[x]['order'])
    setattr(game_config, 'goods_roulette_same_goodsroulette', same_goodsroulette)


def loot_double_f(game_config, config_name, config_value):
    data = {}
    for cfg_id, obj in config_value.iteritems():
        data.setdefault(obj['object_sort'], []).append(cfg_id)
    setattr(game_config, 'loot_double_object_sort', data)


def loot_f(game_config, config_name, config_value):
    all_loot = getattr(game_config, 'loot', {})
    all_loot.update(config_value)

    setattr(game_config, 'loot', all_loot)
