# -*- coding: utf-8 -*- 

# 主要是为了对app进行聚类分析
# 根据LDA的训练模型，输出每一个主题的app列表，列表中包含的是app的ID编号
import os
import json
import math
import string
import numpy as np
from sklearn.cluster import KMeans

# 输出排序后的字典，key为输入文本的行号,value:(index_origin,float_value)
def sort_data(path):
    file=open(path)
    line_num=0
    map_content={}
    for line in file:
        list=[]
        index=0
        for word in line.split():
            if math.isnan(float(word)):
                list.append((index,0.0))
            else:
                list.append((index,float(word)))
            index=index+1
        list.sort(key=lambda x:x[1],reverse=True)
        map_content[str(line_num)]=list
        line_num=line_num+1
    file.close()
    return map_content


# 根据输入的index返回单词,input{path of dictionary,the index of an object that return}
# output{the word of specific index}
def get_dic(path_dic,position):
    map_dic={}
    file=open(path_dic)
    index=0
    for word in file:
        index=word.split()[0].strip()
        value=word.split()[1].strip()
        map_dic[index]=value
    file.close()
    return map_dic[str(position)]

# output{output a dic,(key:topic_id,value:app_id)},input{key:topic_id,value:lists of reivew_item_id}
def parse_review_to_doc(map_cluster):
    map_dic={}
    # document id mapping
    path="../data/doc_app_id"
    file=open(path)
    for line in file:
        key=line.split()[0].strip()
        value=line.split()[1].strip()
        map_dic[key]=value
    # s=set()
    file.close()
    clustering={}
    for key in map_cluster.keys():
        s=set()
        list_reviews=map_cluster[key]
        for review_item in list_reviews:
            str_review_item=str(review_item)
            app_id=map_dic[str_review_item]
            s.add(app_id)
        clustering[key]=s
    return clustering

# 处理为二维数组输入到K-means算法中运算处理,
# 是否需要将部分的值放入其中进行计算？
def parse_vector(map_content,top_num=5):
    topic_len=len(map_content["0"])
    review_num=len(map_content.keys())
    vector=[0]*review_num
    for key in map_content.keys():
        index_doc=int(key)
        topic_vector=[0]*topic_len
        value=map_content[key]
        for val in value:
            topic_vector[val[0]]=val[1]
        vector[index_doc]=topic_vector
    return vector,topic_len

# key:topic_num ,vlaue:list(index),index:doc_id
# 输入：二维数组的特征向量，进行聚类分析，得出不同类别中的document
# 输出：字典{key：不同的类别的标号，value：作为二维数组的index即document_id}
def K_means(cluster_data,cluster_num=5):
    kmeans=KMeans(n_clusters=cluster_num,n_init=5)
    array=np.array(cluster_data)
    kmeans.fit(array)
    list_cluster=kmeans.predict(array)
    # another way to calculate cluster index
    # list_cluster=kmeans.labels_
    topic_num=len(cluster_data[0])
    map_topic={}
    for i in range(0,topic_num):
        temp_list=[]
        for j in range(0,len(list_cluster)):
            if list_cluster[j]==i:
                temp_list.append(j)
        map_topic[i]=temp_list
    return map_topic

def cluster_K_means(map_contents):
    vector=parse_vector(map_contents)
    map_topic=K_means(vector[0],vector[1])
    return map_topic


# 利用K-means等聚类方法对其实施
def cluster_means(map_content):
    map_topic=cluster_K_means(map_content)
    # print map_topic
    clustering=parse_review_to_doc(map_topic)
    # print clustering
    for key in clustering.keys():
        val=clustering[key]
        lis=""
        for data in val:
            lis=lis+data+" "
        print "topic"+str(key),lis.strip()


# input{key:review_id,value(topic_id,value_pro),已经排过序},output{topic_id,list(app_id)}
def cluster(map_content):
    # topic id:list(reivew_item_id)
    map_cluster={}
    for key in map_content.keys():
        value_list=map_content[key]
        # 找出概率最大的topic   max
        # 此处的聚类方法需要修改，修改为K-means的聚类，而非直接采取最大值的方式
        # 取top5的最大值？

        topic_id=value_list[0][0]

        if topic_id not in map_cluster.keys():
            review_id=[]
            review_id.append(key)
            map_cluster[topic_id]=review_id
        else:
            review_id=map_cluster[topic_id]
            review_id.append(key)
            map_cluster[topic_id]=review_id
    clustering=parse_review_to_doc(map_cluster)
    for key in clustering.keys():
        val=clustering[key]
        lis=""
        for data in val:
            lis=lis+data+" "
        print "topic"+str(key),lis.strip()

def main():

    # path="/home/wangrun/Desktop/Experiment/BTM/BTM1/output/model/k20.pz_d"
    # map=sort_data(path)
    # cluster(map)

    path="../data/k20.pz_d"
    map=sort_data(path)
    cluster_means(map)

if __name__=="__main__":
    main()