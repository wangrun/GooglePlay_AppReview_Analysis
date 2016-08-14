# -*- coding: utf-8 -*-


# 计算topic中permission的具体信息，需要检索app的权限列表，得到某一个类别中permission的分布情况
import os
import sys
import json
import string

# 根据输入的app ID编号，输出app的路径
def find_app_id(app_id):
    root_path="E:/experiment data/Google Play/metadata"
    dirs=os.listdir(root_path)
    for dir in dirs:
        lis_dir=root_path+"/"+dir
        app_dir=os.listdir(lis_dir)
        if app_id+".json" in app_dir:
            return lis_dir+"/"+app_id+".json"

# 根据输入的app ID编号，输出app的权限列表信息
def permission_id(app_id):
    path=find_app_id(app_id)
    if path==None:
        return None
    file=open(path)
    f=json.load(file)
    docid=f["docid"]
    details=f["details"]
    app_details=details["app_details"]
    if "permission" not in app_details.keys():
        return None
    permission=app_details["permission"]
    file.close()
    return permission


# 输入：每一个app的权限信息，统计输出前top_number的权限名称及个数等，默认值为前3个
def permission_max(list_per,top_number=3):
    t=[]
    for data in list_per:
        num=list_per.count(data)
        # num:特定permission在列表中出现的次数
        # data:特定的permission信息，如Send_SMS等
        store=(num,data)
        t.append(store)
    t.sort(key=lambda x:x[0],reverse=True)
    s=set()
    for temp in t:
        s.add(temp)
        if len(s)==top_number:
            break
    return s

# input:每一个主题下的app列表，输出的是每一个主题的特征表示（permission列表）
def cal_topic_permission():
    path="run"
    file=open(path)
    for line in file:
        list_per=[]
        data=line.split()
        for i in range(1,len(data)):
            # 获取特定app ID的权限列表
            permission_app_id=permission_id(data[i])
            if permission_app_id==None:
                continue
            list_per=list_per+permission_app_id
        top_per=permission_max(list_per,top_number=5)
        print data[0]
        for top in top_per:
            # 输入的特定主题下的表示信息：permission的个数及名称
            print top[0],top[1]

# 计算特定的app聚类列表中的app的权限表示，某一个类别中权限的信息
def main():
    cal_topic_permission()

if __name__=="__main__":
    main()