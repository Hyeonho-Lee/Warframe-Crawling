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

pd.options.display.float_format = '{:.0f}'.format

#https://rfriend.tistory.com/494

def write_plot(item):
    get_item = item
    get_path = './item/' + get_item + '/' + get_item + '.csv'
    get_path_0 = './item/' + get_item + '/' + get_item + '.png'
    
    result = pd.read_csv(get_path)
    result_data = pd.DataFrame({'date' : result['last_seen'].apply(lambda x: pd.to_datetime(str(x), format = '%Y-%m-%d')), 'platinum' : result['platinum']})
    
    result_data.set_index(result_data['date'], inplace = True)
    
    for col in result_data.columns:
        if col == 'date':
            del result_data[col]
    
    dayly_data = pd.DataFrame()
    
    dayly_data['dayly_data_min'] = result_data.platinum.resample('1D').min()
    dayly_data['dayly_data_median'] = result_data.platinum.resample('1D').median()
    dayly_data['dayly_data_max'] = result_data.platinum.resample('1D').max()
    dayly_data['dayly_data_mean'] = result_data.platinum.resample('1D').mean()

    save = dayly_data.plot(kind = 'line', title = 'Warframe Data', figsize = (8, 4), legend = True, fontsize = 12, marker = 'o')

    plt.show()
    plt.savefig(get_path_0)
    
    #print(str(get_item) + '그래프를 완성하였습니다.')
    
    return dayly_data
    
#write_plot()
