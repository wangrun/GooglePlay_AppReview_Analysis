# f=open("yyyy")
# str="com.libiitech.littlegirlsalon"
# line_number=0
# for line in f:
#     print len(line.split())
    # for data in line.split():
    #     print len(data)
    #     if data==str:
    #         line_number=line_number+1

# print line_number


# f1=open("../data/doc_app_id")
# s=set()
# for line in f1:
#     # print line.split()[0].strip()
#     s.add(line.split()[1].strip())
#     # for data in line.split():
#     #     print type(data)
#         # s.add(data[1])
# f1.close()
# print len(s)

f=open("yyyy")
x=[]
y=[]
num=0
for line in f:
    if num==0:
        for data in line.split():
            x.append(data)
    if num==7:
        for data in line.split():
            y.append(data)
    num=num+1

f.close()
print len(x),len(y)
count=0
for word in x:
    if word in y:
        count=count+1

print count