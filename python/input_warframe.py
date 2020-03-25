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

def input_item():
    with open('/workspace/crawling/data/json/warframes.json', "r") as json_file:
        json_data = json.load(json_file)

    warframes_data = []

    for i in json_data['warframes']:
        warframes_data.append(str(i["name"]))
    
    return warframes_data