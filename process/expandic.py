# -*- coding: utf-8 -*- 

# 利用NLTK提供的wordnet扩充语义，找出同义词等内容
from nltk.corpus import wordnet as wn

# path="E:/experiment source/dictionary"
# path1="E:/experiment source/assem"

# f1=open(path)
# f2=open(path1)

# map={}
# for line in f1:
#     map[line]=""
# for line in f2:
#     map[line]=""

# for key in map.keys():
#     print key.replace("\n","")

# f1.close()
# f2.close()

# for line in f:
#     word=line.replace("\n","")
#     for syn_word in wn.synsets(word):
#         for lemma in syn_word.lemmas():
#             print lemma.name()

# f.close()

# x=wn.synsets("china")
# print x
# # for m in x.lemmas():
# #     print m.name()

# print wn.synsets('car')
for word in wn.synsets('car'):
    for lemma in word.lemmas():
        print lemma.name()