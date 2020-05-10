import os
import json
import pandas as pd
import numpy as np
from flask import Flask, url_for, render_template, request, redirect, session

#https://www.chartjs.org/
#https://datatables.net/
#https://rpc-flask-app.run.goorm.io/ 홈페이지 사이트
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

def get_all_item():
    all_item = []
    all_item_kr = []
    all_path = []
    all_path_0 = []
    all_path_1 = []

    input_items_0 = input_item('warframes')
    input_items_0_kr = input_item_kr('warframes')

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

    input_items_1 = input_item('weapons')
    input_items_1_kr = input_item_kr('weapons')

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
        
    input_items_2 = input_item('weapons_etc')
    input_items_2_kr = input_item_kr('weapons_etc')

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

    return all_item, all_item_kr, all_path, all_path_0, all_path_1

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

    path = '/workspace/crawling/data/csv/result/{name}.csv'.format(name = csv_name)
    resource = read_csv_file(path)

    result_all = []
    result_value = ''
    types = etc
    
    if types == 'in':
        for i in range(0, len(resource)):
            result = resource['name'][i]
            result_1 = result.replace('_set', '')
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

@app.route('/')
def index():
    
    today_datetime = get_today_date()
    all_top = read_csv('all_top', 'result')
    all_bottom = read_csv('all_bottom', 'result')
    today_top = read_csv('today_top', 'result')
    today_bottom = read_csv('today_bottom', 'result')
    today_volume = read_csv('today_volume', 'result')
    today_all = read_csv('result', 'result')

    all_item, all_item_kr, all_path, all_path_0, all_path_1 = get_all_item()
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
@app.route('/tests')
def tests():
    return render_template('demo_0.html')
######################################################################
@app.route('/result/<get_name>')
def result(get_name):
    result_name = '%s' % get_name
    name = change_to_kr('all_top', 'out', result_name)
    name = name.replace('_set', '')

    input_warframe = input_item('warframes')
    input_weapon = input_item('weapons')
    input_weapon_etc = input_item('weapons_etc')

    get_find = False
    is_warframe = False
    is_weapon = False
    is_weapon_etc = False

    if get_find == False:
        for find in input_warframe:
            if name in find:
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

    if(is_warframe == False and is_weapon == False and is_weapon_etc == False):
        return redirect('/error')

    if get_find == True:
        if(result.empty != True):
            label = 'market'
            xlabels = []
            dataset = []
            xlabels = result['datetime'].tolist()
            xlabels.reverse()
            dataset = result['avg_price'].tolist()
            dataset.reverse()
            return render_template('result.html', **locals())
        else:
            return redirect('/error')

@app.route('/error')
def error():
    return render_template('error.html')

#=======================================================================#
if __name__ == '__main__':
    app.static_folder = 'static'
    app.run(host = '0.0.0.0', port = '8080')