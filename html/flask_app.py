import os
import pandas as pd
from flask import Flask, url_for, render_template, request, redirect, session

#https://niceman.tistory.com/191
#https://rpc-flask-app.run.goorm.io/

#=======================================================================#

def read_csv(path):
    get_path = path
    if os.path.isfile(get_path):
        result = pd.read_csv(get_path, index_col = 0)
        result = result[::-1]
    else:
        print('파일이 없습니다.')
        
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

@app.route('/')
def index():
    return render_template('index.html', text = '안녕!!!!!')

@app.route('/warframe')
def warframe():
    return render_template('warframe.html')

@app.route('/result', methods = ['POST'])
def result():
    
    warframe_name = request.form['warframe']
    name = warframe_name.replace(' ', '_')
    name_csv = name + '_set.csv'
    path = '/workspace/crawling/data/csv/warframe/{name}_set/{name_csv}'.format(name = name, name_csv = name_csv)

    result = read_csv(path)
    html_data = result.to_html(index = False, justify = 'center')

    return html_data

@app.route('/error/404')
def error():
    return render_template('error.html')

#=======================================================================#
if __name__ == '__main__':
    app.static_folder = 'static'
    app.run(host = '0.0.0.0', port = '8080')