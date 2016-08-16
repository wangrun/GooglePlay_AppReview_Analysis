# -*- coding: utf-8 -*- 

import numpy as np
from sklearn.cluster import KMeans

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

def main():
    x=[[0.6,0.4,0.0,0.0],[0.0,0.0,0.7,0.3],[0.5,0.3,0.0,0.2],[0.0,0.0,0.4,0.6],[0.6,0.4,0.0,0.0],[0.0,0.0,0.7,0.3],[0.5,0.3,0.0,0.2],[0.0,0.0,0.4,0.6]]
    num=4
    map_topic=K_means(x,num)
    print map_topic

if __name__=="__main__":
    main()

