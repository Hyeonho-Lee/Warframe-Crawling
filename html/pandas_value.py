import os
import pandas as pd
import numpy as np

def read_csv(path):
    get_path = path
    if os.path.isfile(get_path):
        result = pd.read_csv(get_path, index_col = 0)
        result = result.reset_index()
        result = result[::-1]
    else:
        print('파일이 없습니다.')
        
    return result

def pandas_value(name):
    warframe_name = name
    name = warframe_name.replace(' ', '_')
    name_csv = name + '_set.csv'
    path = '/workspace/crawling/data/csv/warframe/{name}_set/{name_csv}'.format(name = name, name_csv = name_csv)

    result = read_csv(path)

    result['day_before'] = np.nan
    result['yn_before'] = np.nan

    result.loc[0, ['day_before']] = 0.0
    result.loc[0, ['yn_before']] = '●'

    for i in range(1, len(result)):
        value = result['avg_price'][i] - result['avg_price'][i-1]
        result.loc[i, ['day_before']] = value

        yn_value = str(value)[0:1]
        if(yn_value == '-'):
            yn_result = '▼'
            result.loc[i, ['yn_before']] = yn_result
        else:
            if(value == 0.0):
                yn_result = '●'
                result.loc[i, ['yn_before']] = yn_result
            else:
                yn_result = '▲'
                result.loc[i, ['yn_before']] = yn_result

    for col in result.columns:
        if col == 'index':
            del result[col]

    return result