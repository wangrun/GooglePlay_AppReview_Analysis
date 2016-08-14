# -*- coding: utf-8 -*- 

# 主要是为了对app进行聚类分析
# 根据LDA的训练模型，输出每一个主题的app列表，列表中包含的是app的ID编号
import os
import json
import string

# 输出排序后的字典，key为输入文本的行号,value:(index_origin,float_value)
def sort_data(path):
    file=open(path)
    line_num=0
    map_content={}
    for line in file:
        list=[]
        index=0
        for word in line.split():
            list.append((index,float(word)))
            index=index+1
        list.sort(key=lambda x:x[1],reverse=True)
        map_content[str(line_num)]=list
        line_num=line_num+1
    file.close()
    return map_content


# 根据输入的index返回单词,input{path of dictionary,the index of an object that return},output{the word of specific index}
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
    path="/home/wangrun/Desktop/Experiment/doc_app_id"
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
            app_id=map_dic[review_item]
            s.add(app_id)
        clustering[key]=s
    return clustering


# 利用K-means方法对app所属的topic，按照其概率的大小进行聚类
def k_means(map_content,k=4):
    cluster_means={}
    


    return None
    # 带补充该部分函数体的内容


# input{key:review_id,value(topic_id,value_pro),value:},output{topic_id,list(app_id)}
def cluster(map_content):
    # topic id:list(reivew_item_id)
    map_cluster={}
    for key in map_content.keys():
        value_list=map_content[key]
        # 找出概率最大的topic   max

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
    # print ""

def main():
    # path="/home/wangrun/BTM/output/model/k20.pz"
    # path="/home/wangrun/BTM/output/voca.txt"
    # print get_dic(path,5)
    path="/home/wangrun/Desktop/Experiment/BTM/BTM1/output/model/k20.pz_d"
    map=sort_data(path)
    cluster(map)

if __name__=="__main__":
    main()

# path="/home/wangrun/BTM/output/model/k20.pw_z"
# path1="/home/wangrun/BTM/output/voca.txt"
# file=open(path)
# file1=open(path1)
# count=0
# list=[]
# sort_list=[]
# for line in file:
#     for num in line.split():
#         list.append(float(num))
#     sort_list=sorted(list,reverse=True)
#     # list.sort(reverse=True)
#     break

# map={}
# for dic in file1:
#     value=dic.split()
#     # print value[0],value[1]
#     map[value[0].strip()]=value[1]

# for num in range(0,20):
#     val=sort_list[num]
#     index=list.index(val)
#     print map[str(index)],val

# file.close()
# file1.close()
