import os
import pandas as pd
from flask import Flask, url_for, render_template, request, redirect, session
import pandas_value

#https://niceman.tistory.com/191 강의 사이트
#https://rpc-flask-app.run.goorm.io/ 홈페이지 사이트
#https://icons8.com/icons 아이콘 사이트
#https://pixlr.com/e/ 포토샵 사이트

#=======================================================================#

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

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/result', methods = ['POST'])
def result():
    
    warframe_name = request.form['warframe']
    name = warframe_name.replace(' ', '_')
    
    result = pandas_value.pandas_value(name)
    html_data = result.to_html(index = False, justify = 'center')

    return html_data

@app.route('/error/404')
def error():
    return render_template('error.html')

#=======================================================================#
if __name__ == '__main__':
    app.static_folder = 'static'
    app.run(host = '0.0.0.0', port = '8080')