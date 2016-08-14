# GooglePlay_AppReview_Analysis

#目录 file
**描述**：PScout中的permission与sensitive api的映射表

#目录 process
**描述**：分析和处理Google Play的用户评论数据，按照用户评论的特点，将app进行聚类，得出每一个类别中的权限信息
##data
1. contents.json：利用关键词term筛选后的review和app的数据
2. process_data__：去除停用词等，输入到LDA模型中的review数据
3. overall：单词字典
4. wangrun：类别的app集合，[topic,list(app_id)]

##code
1. expandic.py:利用wordnet扩充语义，找出更多的同义词，构建语义字典，输出文件为overall
2. Getreview.py:利用关键词term出现次数，筛选review数据，输出的文件为content.json
3. process_data.py：处理content.json，去除标点符号、停用词等，文件输出至LDA模型中训练,输出文件为 process_data
4. cluster.py：根据LDA的模型训练，输出每一个主题下的app列表信息，列表中的信息指的是app_id，输出文件为wangrun
5. category_permission.py：根据每一个app的权限申请情况，找出不同类别的permission表示

#目录 Review_Crawler
**描述**：抓取Google Play的用户评论数据

1. app_id_lists：存放Google Play的app ID列表，包括140万个app
2. Crawler.py：抓取Google Play的爬虫代码
3. template.json：存储Google Play用户评论数据样式，写入文件的模板
