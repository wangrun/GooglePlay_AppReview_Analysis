# -*- coding: utf-8 -*- 


# 按照permission和sensitive API构建的单词字典，按照review中字典中单词出现的次数，筛选app及其review item
import os
import json
import string


# 根据出现的单词个数，筛选相应的review item
# 从原始抓取的app review数据中，按照关键词出现的频率，筛选出app及其相应的review
def read_json(path,word_lists):
    print path
    file_json=open(path)
    fp=json.load(file_json)
    store_map={}
    num=0
    sum=len(fp)
    for app_id in fp:
        num=num+1
        print num,"     ",sum
        for key in app_id.keys():
            items=app_id[key]
            content_view=[]
            for value in items:
                data=value["review_contents"]
                count=verify(data,word_lists)
                if count>5:
                    content_view.append(data)
                # print "review_contents:",value["review_contents"]
            store_map[key]=content_view
    
    file_new=open("contents.json","w+")
    json.dump(store_map,file_new)
    file_new.close()
    file_json.close()

# 读取字典overall，overall中为加入同义词的名词及名词短语等
def read_dic():
    file_path="E:/experiment source/overall"
    word_list=[]
    dictionary=open(file_path)
    for word in dictionary:
        word_list.append(word.replace("\n",""))
    dictionary.close()
    return word_list

# f在一个字符串data中找出，word_list出现的次数
def verify(data,word_list):
    count=0
    for word in word_list:
        count=count+data.count(word.replace("\n",""))
    return count

# 根据相应的目录获取原始抓取的review路径信息
def parse():
    dir="E:/execution/data"
    files=os.listdir(dir)
    word_lists=read_dic()
    for path in files:
        read_json(dir+"/"+path,word_lists)

# 计算筛选后的review item的数量
def count_revew_after():
    file_path="contents.json"
    f=open(file_path)
    json_open=json.load(f)
    print len(json_open.keys())
    count=0
    for cont in json_open.values():
        count=count+len(cont)
    print count
    # print len(json_open.values())
    f.close()


# count number of app and review  item
def count_id_review():
    file="E:/execution/data"
    count_id=0
    count_review=0
    dirs=os.listdir(file)
    for path in dirs:
        f=open(file+"/"+path)
        fp=json.load(f)
        for id in fp:
            count_id=count_id+1
            for key in id.keys():
                items=id[key]
                count_review=count_review+len(items)
        f.close()
    print "app:",count_id,"reviews:",count_review


def main():
    count_revew_after()

if __name__ == '__main__':
    main()
    