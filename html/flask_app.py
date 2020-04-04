import os
import pandas as pd
import numpy as np
from flask import Flask, url_for, render_template, request, redirect, session

#http://dnfnow.xyz/howto
#https://niceman.tistory.com/191 강의 사이트
#https://rpc-flask-app.run.goorm.io/ 홈페이지 사이트
#https://icons8.com/icons 아이콘 사이트
#https://pixlr.com/e/ 포토샵 사이트
#https://www.highcharts.com/forum/viewtopic.php?t=36318
#https://infinitt.tistory.com/38
#flask highcharts example


#=======================================================================#

def read_csv(name, types):
    names = name + '_set'
    name_csv = names + '.csv'
    path = '/workspace/crawling/data/csv/{types}/{name}/{name_csv}'.format(types = types, name = names, name_csv = name_csv)
    get_path = path
    if os.path.isfile(get_path):
        result = pd.read_csv(get_path, index_col = 0)
        result = result.reset_index()
        result = result[::-1]
        return result
    else:
        result = pd.DataFrame()
        return result
        #print('파일이 없습니다.')

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
    return render_template('index.html', text = '안녕!!!!!')

@app.route('/warframe')
def warframe():
    return render_template('warframe.html')

@app.route('/weapon')
def weapon():
    return render_template('weapon.html')
######################################################################
@app.route('/tests')
def tests():
    return render_template('demo_0.html')
######################################################################
#https://apt-info.github.io/%EA%B0%9C%EB%B0%9C/python-flask4-chart/
@app.route('/result_warframe', methods = ['POST'])
def result_warframe():
    
    warframe_name = request.form['warframe']
    name = warframe_name.replace(' ', '_')
    
    result = read_csv(name, 'warframe')
    
    if(result.empty == True):
        return redirect('/error/404')
    else:
        label = 'market'
        xlabels = []
        dataset = []
        xlabels = result['datetime'].tolist()
        xlabels.reverse()
        dataset = result['avg_price'].tolist()
        dataset.reverse()
        print(warframe_name)
        return render_template('result.html', **locals())

@app.route('/result_weapon', methods = ['POST'])
def result_weapon():
    
    weapon_name = request.form['weapon']
    name = weapon_name.replace(' ', '_')
    
    result = read_csv(name, 'weapon')
    
    if(result.empty == True):
        return redirect('/error/404')
    else:
        html_data = result.to_html(index = False, justify = 'center')
        return html_data

@app.route('/error/404')
def error():
    return render_template('error.html')

#=======================================================================#
if __name__ == '__main__':
    app.static_folder = 'static'
    app.run(host = '0.0.0.0', port = '8080')