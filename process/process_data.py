# -*- coding: utf-8 -*- 

import sys
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

# 处理content.json，去除stopwor、一些标点符号等，输出的文件直接放入LDA模型中训练
# 输出的文件为process_data
def read_json(path):
    file=open(path)
    read_json=json.load(file)
    keys=read_json.keys()
    line_num=0
    review_appid=[]
    tokenizer=RegexpTokenizer(r'\w+')
    for key in keys:
        list_content=read_json[key]
        for item in list_content:
            # 增加每个review item的ID编号
            tag=(line_num,key)
            line_num=line_num+1
            review_appid.append(tag)

            review_item=tokenizer.tokenize(item)
            stop_word=stopwords.words('english')
            str_contents=""
            for word in review_item:
                if word.lower() not in stop_word:
                    str_contents=str_contents+word+" "
            print str_contents.strip()
    file.close()
    return review_appid

def s():
    str="Hello, man after above@!$%^&*, ji's'"
    tokenizer=RegexpTokenizer(r'\w+')
    m=tokenizer.tokenize(str)
    print type(m),m

def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    # s()
    path="contents.json"
    t=read_json(path)
    for pair in t:
        print pair[0],pair[1]

if __name__=="__main__":
    main()