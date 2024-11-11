import json
import pprint
import re
import random
from pandas import *

def romaji_list():
    data = read_csv("hiragana.csv")
    list_ = data['romaji'].tolist()
    return list_
n = random.randint(0,105)

def rom(char):
    f = open('hiragana.json', encoding="utf-8") 
    data = json.load(f) 
    for i in range(105):
        if char == data[i]['roumaji']:
            kana = data[i]['kana']
            roumaji = data[i]['roumaji']
            type_ = data[i]['type']
            f.close() 
            return kana, roumaji, type_

    #kana = data[n]['kana']
    #roumaji = data[n]['roumaji']
    #type_ = data[n]['type']

