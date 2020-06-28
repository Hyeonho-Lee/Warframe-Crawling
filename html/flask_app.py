import os
import json
import datetime
import pandas as pd
import numpy as np
from flask import Flask, url_for, render_template, request, redirect, session

#https://www.chartjs.org/
#https://datatables.net/
#https://rpc-flask-app.run.goorm.io/ 홈페이지 사이트
#https://rpc-test-app.run.goorm.io/ 테스트 사이트
#https://icons8.com/icons 아이콘 사이트
#https://pixlr.com/e/ 포토샵 사이트
#https://zamezzz.tistory.com/309
#https://offbyone.tistory.com/260

#=======================================================================#

def read_csv_file(path):
    get_path = path
    if os.path.isfile(get_path):
        result = pd.read_csv(get_path, index_col = 0)
        result = result.reset_index()
        return result
    else:
        print('파일이 없습니다.')

def read_csv(name, types):
    names = name + '_set'
    name_csv = names + '.csv'
    path = ''
    if types == 'result':
        name_csv = name + '.csv'
        path = '/workspace/crawling/data/csv/{types}/{name_csv}'.format(types = types, name_csv = name_csv)
    elif types == 'weapon_etc':
        name_csv = name + '.csv'
        path = '/workspace/crawling/data/csv/weapon/{names}/{name_csv}'.format(names = name, name_csv = name_csv)
        print(path)
    elif types == 'aura_mods':
        name_csv = name + '.csv'
        path = '/workspace/crawling/data/csv/mod/{names}/{name_csv}'.format(names = name, name_csv = name_csv)
        print(path)
    elif types == 'warframe_mods':
        name_csv = name + '.csv'
        path = '/workspace/crawling/data/csv/mod/{names}/{name_csv}'.format(names = name, name_csv = name_csv)
        print(path)
    else:
        path = '/workspace/crawling/data/csv/{types}/{name}/{name_csv}'.format(types = types, name = names, name_csv = name_csv)
    get_path = path
    if os.path.isfile(get_path):
        result = pd.read_csv(get_path, index_col = 0)
        result = result.reset_index()
        if types != 'result':
            result = result[::-1]
        return result
    else:
        result = pd.DataFrame()
        return result

def input_item(etc):
    item = str(etc)
    path = '/workspace/crawling/data/json/{etc}.json'.format(etc = item)
    with open(path, "r") as json_file:
        json_data = json.load(json_file)

    name_data = []

    for i in json_data[item]:
        name_data.append(str(i["name"]))

    return name_data

def input_item_kr(etc):
    item = str(etc)
    path = '/workspace/crawling/data/json/{etc}.json'.format(etc = item)
    with open(path, "r") as json_file:
        json_data = json.load(json_file)

    name_data = []

    for i in json_data[item]:
        name_data.append(str(i["kr_name"]))

    return name_data

def input_item_type(etc):
    item = str(etc)
    path = '/workspace/crawling/data/json/{etc}.json'.format(etc = item)
    with open(path, "r") as json_file:
        json_data = json.load(json_file)

    name_data = []

    for i in json_data[item]:
        name_data.append(str(i["type"]))

    return name_data

def get_all_item():
    all_item = []
    all_item_kr = []
    all_path = []
    all_path_0 = []
    all_path_1 = []
    all_type = []
    all_type_kr = []

    input_items_0 = input_item('warframes')
    input_items_0_kr = input_item_kr('warframes')
    input_types_0 = input_item_type('warframes')

    for i, v in enumerate(input_items_0):
        item = str(v) + '_set'
        path = '/workspace/crawling/data/csv/warframe/' + item + '/' + item + '.csv'
        path_0 = '/workspace/crawling/data/csv/warframe/' + item
        img = str(v.title())
        path_1 = 'image/item_image/warframe/' + img + '/' + img + '.png'
        all_item.append(item)
        all_path.append(path)
        all_path_0.append(path_0)
        all_path_1.append(path_1)

    for i, v in enumerate(input_items_0_kr):
        item = str(v)
        all_item_kr.append(item)

    for i, v in enumerate(input_types_0):
        item = str(v)
        all_type.append(item)

    input_items_1 = input_item('weapons')
    input_items_1_kr = input_item_kr('weapons')
    input_types_1 = input_item_type('weapons')

    for i, v in enumerate(input_items_1):
        item = str(v) + '_set'
        path = '/workspace/crawling/data/csv/weapon/' + item + '/' + item + '.csv'
        path_0 = '/workspace/crawling/data/csv/weapon/' + item
        img = str(v.title())
        path_1 = 'image/item_image/weapon/' + img + '/' + img + '.png'
        all_item.append(item)
        all_path.append(path)
        all_path_0.append(path_0)
        all_path_1.append(path_1)

    for i, v in enumerate(input_items_1_kr):
        item = str(v)
        all_item_kr.append(item)

    for i, v in enumerate(input_types_1):
        item = str(v)
        all_type.append(item)

    input_items_2 = input_item('weapons_etc')
    input_items_2_kr = input_item_kr('weapons_etc')
    input_types_2 = input_item_type('weapons_etc')

    for i, v in enumerate(input_items_2):
        item = str(v)
        path = '/workspace/crawling/data/csv/weapon/' + item + '/' + item + '.csv'
        path_0 = '/workspace/crawling/data/csv/weapon/' + item
        img = str(v.title())
        path_1 = 'image/item_image/weapon/' + img + '/' + img + '.png'
        all_item.append(item)
        all_path.append(path)
        all_path_0.append(path_0)
        all_path_1.append(path_1)

    for i, v in enumerate(input_items_2_kr):
        item = str(v)
        all_item_kr.append(item)

    for i, v in enumerate(input_types_2):
        item = str(v)
        all_type.append(item)

    input_items_3 = input_item('aura_mods')
    input_items_3_kr = input_item_kr('aura_mods')
    input_types_3 = input_item_type('aura_mods')

    for i, v in enumerate(input_items_3):
        item = str(v)
        path = '/workspace/crawling/data/csv/mod/' + item + '/' + item + '.csv'
        path_0 = '/workspace/crawling/data/csv/mod/' + item
        img = str(v.title())
        path_1 = 'image/item_image/mod/' + img + '/' + img + '.png'
        all_item.append(item)
        all_path.append(path)
        all_path_0.append(path_0)
        all_path_1.append(path_1)

    for i, v in enumerate(input_items_3_kr):
        item = str(v)
        all_item_kr.append(item)

    for i, v in enumerate(input_types_3):
        item = str(v)
        all_type.append(item)

    input_items_4 = input_item('warframe_mods')
    input_items_4_kr = input_item_kr('warframe_mods')
    input_types_4 = input_item_type('warframe_mods')

    for i, v in enumerate(input_items_4):
        item = str(v)
        path = '/workspace/crawling/data/csv/mod/' + item + '/' + item + '.csv'
        path_0 = '/workspace/crawling/data/csv/mod/' + item
        img = str(v.title())
        path_1 = 'image/item_image/mod/' + img + '/' + img + '.png'
        all_item.append(item)
        all_path.append(path)
        all_path_0.append(path_0)
        all_path_1.append(path_1)

    for i, v in enumerate(input_items_4_kr):
        item = str(v)
        all_item_kr.append(item)

    for i, v in enumerate(input_types_4):
        item = str(v)
        all_type.append(item)

    for i, v in enumerate(all_item_kr):
        if all_type[i] == "primary":
            all_type_kr.append("주무기")
        elif all_type[i] == "secondary":
            all_type_kr.append("보조무기")
        elif all_type[i] == "melee":
            all_type_kr.append("근접무기")
        elif all_type[i] == "archwing":
            all_type_kr.append("아크윙")
        elif all_type[i] == "warframe":
            all_type_kr.append("워프레임")
        elif all_type[i] == "aura_mod":
            all_type_kr.append("워프레임 모드")
        elif all_type[i] == "warframe_mod":
            all_type_kr.append("워프레임 모드")
        else:
            all_type_kr.append("기타")

    return all_item, all_item_kr, all_path, all_path_0, all_path_1, all_type, all_type_kr

def change_to_kr(csv_name, etc, text):
    item_name = []
    item_en_name = []
    item_kr_name = []

    with open('/workspace/crawling/data/json/warframes.json', 'r') as file:
        json_data = json.load(file)
    result_data = json_data['warframes']
    with open('/workspace/crawling/data/json/weapons.json', 'r') as file_1:
        json_data_1 = json.load(file_1)
    result_data_1 = json_data_1['weapons']
    with open('/workspace/crawling/data/json/weapons_etc.json', 'r') as file_2:
        json_data_2 = json.load(file_2)
    result_data_2 = json_data_2['weapons_etc']
    with open('/workspace/crawling/data/json/aura_mods.json', 'r') as file_3:
        json_data_3 = json.load(file_3)
    result_data_3 = json_data_3['aura_mods']
    with open('/workspace/crawling/data/json/warframe_mods.json', 'r') as file_4:
        json_data_4 = json.load(file_4)
    result_data_4 = json_data_4['warframe_mods']

    for i in range(0, len(result_data)):
        result = result_data[i]['name']
        en_result = result_data[i]['en_name']
        kr_result = result_data[i]['kr_name']
        item_name.append(str(result))
        item_en_name.append(str(en_result))
        item_kr_name.append(str(kr_result))

    for i in range(0, len(result_data_1)):
        result = result_data_1[i]['name']
        en_result = result_data_1[i]['en_name']
        kr_result = result_data_1[i]['kr_name']
        item_name.append(str(result))
        item_en_name.append(str(en_result))
        item_kr_name.append(str(kr_result))

    for i in range(0, len(result_data_2)):
        result = result_data_2[i]['name']
        en_result = result_data_2[i]['en_name']
        kr_result = result_data_2[i]['kr_name']
        item_name.append(str(result))
        item_en_name.append(str(en_result))
        item_kr_name.append(str(kr_result))
    
    for i in range(0, len(result_data_3)):
        result = result_data_3[i]['name']
        en_result = result_data_3[i]['en_name']
        kr_result = result_data_3[i]['kr_name']
        item_name.append(str(result))
        item_en_name.append(str(en_result))
        item_kr_name.append(str(kr_result))
    
    for i in range(0, len(result_data_4)):
        result = result_data_4[i]['name']
        en_result = result_data_4[i]['en_name']
        kr_result = result_data_4[i]['kr_name']
        item_name.append(str(result))
        item_en_name.append(str(en_result))
        item_kr_name.append(str(kr_result))

    path = '/workspace/crawling/data/csv/result/{name}.csv'.format(name = csv_name)
    resource = read_csv_file(path)

    result_all = []
    result_value = ''
    types = etc

    if types == 'in':
        for i in range(0, len(resource)):
            result = resource['name'][i]
            results = str(result)
            result_1 = results.replace('_set', '')
            if result_1 in item_name:
                count = item_name.index(result_1)
                re_text = item_kr_name[count]
                result_all.append(re_text)
        return result_all
    elif types == 'out':
        input_text = text
        if input_text in item_kr_name:
            count = item_kr_name.index(input_text)
            re_text = item_name[count]
            result_value = re_text + '_set'
        else:
            result_value = input_text
        return result_value

def get_today_date():
    result = read_csv('result', 'result')
    date = result['datetime']
    datetime = str(date[0])
    return datetime

def get_visit():
    today = datetime.datetime.now()
    year = str(today.year)
    month = str(today.month)
    day = str(today.day)

    if len(month) == 1:
        month = '0' + month

    visit_count = session.get('visit_count') != 1
    
    with open('/workspace/crawling/data/json/visitant.json', "r") as json_visit:
        visit_data = json.load(json_visit)
    
    if visit_count:
        session['visit_count'] = 1

        query_1 = dict()
        year_month = dict()
        year_month["year_month"] = year + month
        year_month["day"] = day
        result = session.get('visit_count')
        year_month["count"] = visit_data["date"]["count"] + 1
        query_1["date"] = year_month

        with open('/workspace/crawling/data/json/visitant.json', 'w', encoding='utf-8') as update_visit:
            json.dump(query_1, update_visit, indent = 4)
    
    with open('/workspace/crawling/data/json/visitant.json', "r") as json_visits:
        visits_data = json.load(json_visits)
    result = visits_data["date"]["count"]
    return result
"""
if os.path.isdir(get_path_0):
    make_file(get_path)
else:
    #print('폴더가 없음으로 새로 만들었습니다.')
    os.makedirs(get_path_0)
    make_file(get_path)
"""
#=======================================================================#

app = Flask(__name__)
random = os.urandom(24)
app.secret_key = random

@app.route('/')
def index():

    visit_count = get_visit()

    today_datetime = get_today_date()
    all_top = read_csv('all_top', 'result')
    all_bottom = read_csv('all_bottom', 'result')
    today_top = read_csv('today_top', 'result')
    today_bottom = read_csv('today_bottom', 'result')
    today_volume = read_csv('today_volume', 'result')
    today_all = read_csv('result', 'result')

    all_item, all_item_kr, all_path, all_path_0, all_path_1, all_type, all_type_kr = get_all_item()
    def find_path(name, types):
        if types == 'path':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path = all_path[i]
                    return path
        elif types == 'path_0':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path_0 = all_path_0[i]
                    return path_0
        elif types == 'path_1':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path_1 = all_path_1[i]
                    return path_1

    a_top_name = []
    a_top_kr_name = []
    a_top_price = []
    a_top_before = []
    a_top_percent = []
    a_top_path = []
    a_top_path_0 = []
    a_top_path_1 = []
    a_top_name = all_top['name'].tolist()
    a_top_kr_name = change_to_kr('all_top', 'in', '')
    a_top_price = all_top['avg_price'].tolist()
    a_top_before = all_top['day_before'].tolist()
    a_top_percent = all_top['day_percent'].tolist()
    for i in a_top_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        a_top_path.append(str(result))
        a_top_path_0.append(str(result_0))
        a_top_path_1.append(str(result_1))

    a_bottom_name = []
    a_bottom_kr_name = []
    a_bottom_price = []
    a_bottom_before = []
    a_bottom_percent = []
    a_bottom_path = []
    a_bottom_path_0 = []
    a_bottom_path_1 = []
    a_bottom_name = all_bottom['name'].tolist()
    a_bottom_kr_name = change_to_kr('all_bottom', 'in', '')
    a_bottom_price = all_bottom['avg_price'].tolist()
    a_bottom_before = all_bottom['day_before'].tolist()
    a_bottom_percent = all_bottom['day_percent'].tolist()
    for i in a_bottom_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        a_bottom_path.append(str(result))
        a_bottom_path_0.append(str(result_0))
        a_bottom_path_1.append(str(result_1))

    t_top_name = []
    t_top_kr_name = []
    t_top_price = []
    t_top_before = []
    t_top_percent = []
    t_top_path = []
    t_top_path_0 = []
    t_top_path_1 = []
    t_top_name = today_top['name'].tolist()
    t_top_kr_name = change_to_kr('today_top', 'in', '')
    t_top_price = today_top['avg_price'].tolist()
    t_top_before = today_top['day_before'].tolist()
    t_top_percent = today_top['day_percent'].tolist()
    for i in t_top_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        t_top_path.append(str(result))
        t_top_path_0.append(str(result_0))
        t_top_path_1.append(str(result_1))

    t_bottom_name = []
    t_bottom_kr_name = []
    t_bottom_price = []
    t_bottom_before = []
    t_bottom_percent = []
    t_bottom_path = []
    t_bottom_path_0 = []
    t_bottom_path_1 = []
    t_bottom_name = today_bottom['name'].tolist()
    t_bottom_kr_name = change_to_kr('today_bottom', 'in', '')
    t_bottom_price = today_bottom['avg_price'].tolist()
    t_bottom_before = today_bottom['day_before'].tolist()
    t_bottom_percent = today_bottom['day_percent'].tolist()
    for i in t_bottom_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        t_bottom_path.append(str(result))
        t_bottom_path_0.append(str(result_0))
        t_bottom_path_1.append(str(result_1))

    t_all_name = []
    t_all_kr_name = []
    t_all_price = []
    t_all_before = []
    t_all_befores = []
    t_all_volume = []
    t_all_date = []
    t_all_percent = []
    t_all_path = []
    t_all_path_0 = []
    t_all_path_1 = []
    t_all_name = today_all['name'].tolist()
    t_all_name_count = len(t_all_name)
    t_all_kr_name = change_to_kr('result', 'in', '')
    t_all_price = today_all['avg_price'].tolist()
    t_all_before = today_all['day_before'].tolist()
    t_all_befores = today_all['yn_before'].tolist()
    t_all_volume = today_all['volume'].tolist()
    t_all_date = today_all['datetime'].tolist()
    t_all_percent = today_all['day_percent'].tolist()
    for i in t_all_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        t_all_path.append(str(result))
        t_all_path_0.append(str(result_0))
        t_all_path_1.append(str(result_1))

    label = '가장 많은 거래량'
    xlabels = []
    dataset = []
    xlabel = today_volume['name'].tolist()
    xlabels = change_to_kr('today_volume', 'in', '')
    dataset = today_volume['volume'].tolist()

    return render_template('index.html', **locals())

######################################################################
@app.route('/tests/')
def tests():
    return render_template('demo_0.html')
######################################################################
@app.route('/result/<get_name>/')
def result(get_name):
    visit_count = get_visit()
    all_item, all_item_kr, all_path, all_path_0, all_path_1, all_type, all_type_kr = get_all_item()
    def find_path(name, types):
        if types == 'path':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path = all_path[i]
                    return path
        elif types == 'path_0':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path_0 = all_path_0[i]
                    return path_0
        elif types == 'path_1':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path_1 = all_path_1[i]
                    return path_1

    input_warframe = input_item('warframes')
    input_weapon = input_item('weapons')
    input_weapon_etc = input_item('weapons_etc')
    input_aura_mods = input_item('aura_mods')
    input_warframe_mods = input_item('warframe_mods')

    result_name = '%s' % get_name
    for i, v in enumerate(all_item_kr):
        if str(v) == result_name:
            result_name = all_item[i]
    name = result_name.replace('_set', '')

    name_set = name.replace(' ', '_')
    name_sets = name_set + '_set'

    for i, v in enumerate(all_item):
        if str(v) == result_name:
            kr_name = all_item_kr[i]

    for i in input_weapon_etc:
        if str(name) in i:
            name_sets = name

    for i in input_aura_mods:
        if str(name) in i:
            name_sets = name
    
    for i in input_warframe_mods:
        if str(name) in i:
            name_sets = name

    search_path = find_path(name_sets, 'path')
    search_path_0 = find_path(name_sets, 'path_0')
    search_path_1 = find_path(name_sets, 'path_1')

    get_find = False
    is_warframe = False
    is_weapon = False
    is_weapon_etc = False
    is_aura_mods = False
    is_warframe_mods = False

    if get_find == False:
        for finds in input_warframe:
            if name in finds:
                result = read_csv(name, 'warframe')
                get_find = True
                is_warframe = True
                break

    if get_find == False:
        for finds in input_weapon:
            if name in finds:
                result = read_csv(name, 'weapon')
                get_find = True
                is_weapon = True
                break

    if get_find == False:
        for finds in input_weapon_etc:
            if name in finds:
                result = read_csv(name, 'weapon_etc')
                get_find = True
                is_weapon_etc = True
                break

    if get_find == False:
        for finds in input_aura_mods:
            if name in finds:
                result = read_csv(name, 'aura_mods')
                get_find = True
                is_aura_mods = True
                break
    
    if get_find == False:
        for finds in input_warframe_mods:
            if name in finds:
                result = read_csv(name, 'warframe_mods')
                get_find = True
                is_aura_mods = True
                break

    if(is_warframe == False and is_weapon == False and is_weapon_etc == False and is_aura_mods == False and is_warframe_mods == False):
        return redirect('/error')

    if get_find == True:
        if(result.empty != True):

            today_datetime = get_today_date()

            label = 'market'
            xlabels = []
            dataset = []
            xlabels = result['datetime'].tolist()
            xlabels.reverse()
            dataset = result['avg_price'].tolist()
            dataset.reverse()

            all_datetime = result['datetime'].tolist()
            all_price = result['avg_price'].tolist()
            all_volume = result['volume'].tolist()
            all_day_before = result['day_before'].tolist()
            all_yn_before = result['yn_before'].tolist()
            all_day_percent = result['day_percent'].tolist()
            all_count = len(all_datetime)

            return render_template('result.html', **locals())
        else:
            return redirect('/error')

@app.route('/error')
def error():
    visit_count = get_visit()
    all_item, all_item_kr, all_path, all_path_0, all_path_1, all_type, all_type_kr = get_all_item()
    return render_template('error.html', **locals())

######################################################################
@app.route('/notice/')
def notice():
    visit_count = get_visit()
    all_item, all_item_kr, all_path, all_path_0, all_path_1, all_type, all_type_kr = get_all_item()
    
    path = '/workspace/crawling/data/json/notice_data.json'
    with open(path, "r", encoding="UTF-8") as json_file:
        json_data = json.load(json_file, strict = False)
        json_datas = json.dumps(json_data, ensure_ascii=False)

    index = []
    image = []
    write = []
    subject = []
    contents = []
    contents_image = []
    date = []
    len_data = len(json_data["notice"])
    
    for i in json_data["notice"]:
        index.append(i["index"])
        image.append(i["image"])
        write.append(i["write"])
        subject.append(i["subject"])
        contents.append(i["contents"])
        contents_image.append(i["contents_image"])
        date.append(i["date"])
    
    index.reverse()
    image.reverse()
    write.reverse()
    subject.reverse()
    contents.reverse()
    contents_image.reverse()
    date.reverse()
    
    return render_template('notice.html', **locals())

#=======================================================================#

@app.route('/temp/')
def temp():
    visit_count = get_visit()
    all_item, all_item_kr, all_path, all_path_0, all_path_1, all_type, all_type_kr = get_all_item()
    
    return render_template('temp.html', **locals())

#=======================================================================#
@app.route('/category/')
def category():

    visit_count = get_visit()
    all_item, all_item_kr, all_path, all_path_0, all_path_1, all_type, all_type_kr = get_all_item()

    type_primary_item = []
    type_primary_item_kr = []
    type_primary_path = []
    type_primary_path_0 = []
    type_primary_path_1 = []
    type_primary_type = []
    type_primary_type_kr = []
    type_primary_len = 0

    type_secondary_item = []
    type_secondary_item_kr = []
    type_secondary_path = []
    type_secondary_path_0 = []
    type_secondary_path_1 = []
    type_secondary_type = []
    type_secondary_type_kr = []
    type_secondary_len = 0

    type_melee_item = []
    type_melee_item_kr = []
    type_melee_path = []
    type_melee_path_0 = []
    type_melee_path_1 = []
    type_melee_type = []
    type_melee_type_kr = []
    type_melee_len = 0

    type_warframe_item = []
    type_warframe_item_kr = []
    type_warframe_path = []
    type_warframe_path_0 = []
    type_warframe_path_1 = []
    type_warframe_type = []
    type_warframe_type_kr = []
    type_warframe_len = 0

    type_warframe_mod_item = []
    type_warframe_mod_item_kr = []
    type_warframe_mod_path = []
    type_warframe_mod_path_0 = []
    type_warframe_mod_path_1 = []
    type_warframe_mod_type = []
    type_warframe_mod_type_kr = []
    type_warframe_mod_len = 0

    type_etc_item = []
    type_etc_item_kr = []
    type_etc_path = []
    type_etc_path_0 = []
    type_etc_path_1 = []
    type_etc_type = []
    type_etc_type_kr = []
    type_etc_len = 0

    for i, v in enumerate(all_item_kr):
        if all_type_kr[i] == "주무기":
            type_primary_item.append(all_item[i])
            type_primary_item_kr.append(all_item_kr[i])
            type_primary_path.append(all_path[i])
            type_primary_path_0.append(all_path_0[i])
            type_primary_path_1.append(all_path_1[i])
            type_primary_type.append(all_type[i])
            type_primary_type_kr.append(all_type_kr[i])
        elif all_type_kr[i] == "보조무기":
            type_secondary_item.append(all_item[i])
            type_secondary_item_kr.append(all_item_kr[i])
            type_secondary_path.append(all_path[i])
            type_secondary_path_0.append(all_path_0[i])
            type_secondary_path_1.append(all_path_1[i])
            type_secondary_type.append(all_type[i])
            type_secondary_type_kr.append(all_type_kr[i])
        elif all_type_kr[i] == "근접무기":
            type_melee_item.append(all_item[i])
            type_melee_item_kr.append(all_item_kr[i])
            type_melee_path.append(all_path[i])
            type_melee_path_0.append(all_path_0[i])
            type_melee_path_1.append(all_path_1[i])
            type_melee_type.append(all_type[i])
            type_melee_type_kr.append(all_type_kr[i])
        elif all_type_kr[i] == "워프레임":
            type_warframe_item.append(all_item[i])
            type_warframe_item_kr.append(all_item_kr[i])
            type_warframe_path.append(all_path[i])
            type_warframe_path_0.append(all_path_0[i])
            type_warframe_path_1.append(all_path_1[i])
            type_warframe_type.append(all_type[i])
            type_warframe_type_kr.append(all_type_kr[i])
        elif all_type_kr[i] == "워프레임 모드":
            type_warframe_mod_item.append(all_item[i])
            type_warframe_mod_item_kr.append(all_item_kr[i])
            type_warframe_mod_path.append(all_path[i])
            type_warframe_mod_path_0.append(all_path_0[i])
            type_warframe_mod_path_1.append(all_path_1[i])
            type_warframe_mod_type.append(all_type[i])
            type_warframe_mod_type_kr.append(all_type_kr[i])
        else:
            type_etc_item.append(all_item[i])
            type_etc_item_kr.append(all_item_kr[i])
            type_etc_path.append(all_path[i])
            type_etc_path_0.append(all_path_0[i])
            type_etc_path_1.append(all_path_1[i])
            type_etc_type.append(all_type[i])
            type_etc_type_kr.append(all_type_kr[i])

    type_primary_len = len(type_primary_item)
    type_secondary_len = len(type_secondary_item)
    type_melee_len = len(type_melee_item)
    type_warframe_len = len(type_warframe_item)
    type_warframe_mod_len = len(type_warframe_mod_item)
    type_etc_len = len(type_etc_item)

    print(type_primary_len, type_secondary_len, type_melee_len, type_warframe_len, type_warframe_mod_len, type_etc_len)

    return render_template('category.html', **locals())

#=======================================================================#
if __name__ == '__main__':
    app.static_folder = 'static'
    app.run(host = '0.0.0.0', port = '5000', debug=True)