import cluster
import string


path="../data/k20.pz_d"
map=cluster.sort_data(path)
map_topic=cluster.cluster_K_means(map)

path_dic="../data/process_data"
f=open(path_dic)
map_data={}
count=0
for line in f:
    map_data[str(count)]=line
    count=count+1

f.close()

for key in map_topic.keys():
    print "topic",key
    value=map_topic[key]
    for val in value:
        data=map_data[str(val)]
        print data.strip()
    print "\n"
