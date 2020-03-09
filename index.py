import os
import re
import time
import datetime
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dateutil.parser import parse
from bs4 import BeautifulSoup as bs
from selenium import webdriver

######################################################
import input_warframe
import data_result
######################################################

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless') 
chrome_options.add_argument('--disable-gpu') 
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--lang=ko_KR')

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)
    #'/usr/bin/chromedriver'
    #'/home/prohenho7138/Downloads/chromedriver'
driver.implicitly_wait(1)

def warframe_crawling(chrome, item, path, path_0):
    
    driver = chrome
    get_item = item
    get_path = path
    get_path_0 = path_0
    
    site = 'https://warframe.market/items/' + get_item + '_set'
    driver.get(site)

    html = driver.page_source
    soup = bs(html, 'html.parser')

    result = soup.find_all('script', {'id': 'application-state'})

    with open('./warframe_data.json', 'w') as file:
        data = str(result)
        text = data.replace('[<script id="application-state" type="application/json">', '')
        text_1 = text.replace('</script>]', '')
        json_data = json.loads(text_1)
        json_data_1 = json.dumps(json_data, indent = 4)
        file.write(json_data_1)

    warframe_data = json_data_1

    json_data = json.loads(warframe_data)
    #print('데이터를 불러왔습니다.')

    result_data = pd.DataFrame(json_data['payload']['orders'])

    last_seen = []
    user_data = []
    status_data = []
    platinum_data = []
    order_type_data = []

    for i in result_data['user']:
        date_cut = str(i['last_seen'])
        last_seen.append(date_cut[0:10])
        user_data.append(str(i['ingame_name']))
        status_data.append(str(i['status']))

    for i in result_data['platinum']:
        platinum_data.append(str(i))

    for i in result_data['order_type']:
        order_type_data.append(str(i))

    all_data_list = pd.DataFrame({'last_seen' : last_seen, 'user' : user_data, 'status_data' : status_data, 'platinum' : platinum_data, 'order_type' : order_type_data})

    result = all_data_list[(all_data_list['status_data'] == 'ingame') & (all_data_list['order_type'] == 'sell') | (all_data_list['status_data'] == 'online') & (all_data_list['order_type'] == 'sell')]

    result = result.sort_values(by = ['platinum'], axis = 0).head(15) 
    
    def make_file(path):
        get_path = path
        if os.path.isfile(get_path):
            result.to_csv(get_path, mode = 'a', header = False)
            re_result = pd.read_csv(get_path, index_col = 0)
            all_result = re_result.drop_duplicates('user', keep = 'first')
            all_results = all_result[all_result.last_seen != "None"]
            all_results.to_csv(get_path, mode = 'w')
            #print('데이터 업데이트를 완료했습니다.')
        else:
            result.to_csv(get_path, mode = 'w')
            #print('새로운 데이터를 저장했습니다.') 
    
    if os.path.isdir(get_path_0):
        make_file(get_path)
    else:
        #print('폴더가 없음으로 새로 만들었습니다.')
        os.makedirs(get_path_0)
        make_file(get_path)
    
    print(str(get_item) + ' 업데이트를 하였습니다.')
        
    driver.execute_script('window.open("about:blank", "_blank");')
    driver.close()
    
    tabs = driver.window_handles
    driver.switch_to_window(tabs[-1])
    
    return driver
######################################################

#https://dvpzeekke.tistory.com/1

startTime = time.time()

input_items = input_warframe.input_item()


for i, v in enumerate(input_items):
    item = str(v)
    path = './item/' + item + '/' + item + '.csv'
    path_0 = './item/' + item
    
    driver = warframe_crawling(driver, item, path, path_0)
    save_png = data_result.write_plot(item)
    endTime = time.time() - startTime
    print(str(round(i / len(input_items) * 100)) + "% 완료했습니다. 시간: " + str(round(endTime)) + "초")

"""
item = 'saryn_prime'
path = './item/' + item + '/' + item + '.csv'
path_0 = './item/' + item
    
warframe_crawling(item, path, path_0)
save_png = data_result.write_plot(item)
"""

print("업데이트가 모두 완료했습니다.")
driver.quit()
######################################################