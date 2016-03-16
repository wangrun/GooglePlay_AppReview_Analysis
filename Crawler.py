
import re
import sys
import time
import json
import urllib
import urllib2
from bs4 import BeautifulSoup


def Get_page(id,app_num,path_number):
    url="https://play.google.com/store/getreviews?authuser=0"
    count=0
    values={}
    values['reviewType']='0'
    values['pageNum']='0'
    values['id']=id
    values['reviewSortOrder']='2'
    values['xhr']='1'
    values['hl']='en'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36','Referer':'https://play.google.com/store/apps/details?id='+id+'&hl=en','Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}
    
    # proxy = '127.0.0.1:8787'
    # opener = urllib2.build_opener(urllib2.ProxyHandler({'https':proxy}))
    # urllib2.install_opener(opener)
    
    # data=urllib.urlencode(values)
    # request=urllib2.Request(url,data,headers)
    page=""
    number_path=0
    while 1:
        values['pageNum']=str(count)
        data=urllib.urlencode(values)
        request=urllib2.Request(url,data,headers)
        try:
            response=urllib2.urlopen(request)
            page=response.read()
            if 'div'not in page:
                break
            # print page
            # generate_data(page)
            number_path=write_data(id,page,count,app_num,path_number)
            count=count+1
            time.sleep(8)
            
        except urllib2.HTTPError,e:
            print e.code
            break
        except urllib2.URLError,e:
            print e.reason
            break
        # response=urllib2.urlopen(request)
        # if response
        # page=response.read()
        # print page
        # count=count+1
        # request=urllib2.Request(url,data,headers)
        # if count==4:
        #     break
        # break
    # return page
    return number_path
    
def generate_data(text):
    # path='D:/Project/Expriment/Review/review.txt'
    # f=open(path)
    # text=f.read()
    
    
    
    reload(sys)
    sys.setdefaultencoding('utf-8')
    
    texts=text.decode('utf-8','ignore')
    start=text.index("\u003cdiv")
    end=text.rindex("\u003c/div\u003e")
    com_text=texts[start:end]
    
    com_text = com_text.replace('\u003c', '<')
    com_text = com_text.replace('\u003e', '>')
    com_text = com_text.replace('\u003d', '=')
    com_text = com_text.replace('\u003a', ':')
    com_text = com_text.replace('\u0026', '&')
    com_text = com_text.replace('\\"', '"')
    com_text = com_text.replace('\\n"', '\n')
    
    comments=com_text.decode('utf-8','ignore')
    # print comments
    
    # review_author_name=re.compile(ur'<span class="author-name"> <a.+?id=(.+?)">(.+?)</a>')
    review_author_name=re.compile(ur'<span class="author-name">(.+?)</span>')
    review_date=re.compile(ur'<span class="review-date">(.+?)</span>')
    review_title=re.compile(ur'<span class="review-title">(.+?)<div')
    
    
    # for i in review_author_name.findall(comments):
    #     print i
    
    author_names=[]
    dates=[]
    review_titles=[]
    review_datas=[]
    
    
    for j in review_author_name.finditer(comments):
        if j is None:
            author_names.append(" ")
        else:
            temp_name=j.group(1)
            if "<a href=" in temp_name:
                st=temp_name.index(">")
                ed=temp_name.rindex("</a>")
                author_names.append(temp_name[st+1:ed])
            else:
                author_names.append(j.group(1))
        
    for m in review_date.finditer(comments):
        if m is None:
            dates.append(" ")
        else:
            dates.append(m.group(1))

    for n in review_title.finditer(comments):
        if n is None:
            review_titles.append(" ")
            review_datas.append(" ")
        else:
            ct=n.group(1).split('</span>')
            if len(ct)==2:
                review_titles.append(ct[0])
                review_datas.append(ct[1])
            else:
                review_titles.append(" ")
                review_datas.append(" ")
    
    return author_names,dates,review_titles,review_datas
    
    
    # author_nameM=review_author_name.search(comments)
    # if author_nameM is not None:
    #     author_id=author_nameM.group(1)
    #     # author_name=author_nameM.group(2)
        
    #     print author_id,author_name
    # dateM=review_date.search(comments)
    # if dateM is not None:
    #     date=dateM.group(1)
        
    #     print date
    # titleM=review_title.search(comments)
    # if titleM is not None:
    #     content=titleM.group(1).split('</span>')
    #     if len(content)==2:
    #         title=content[0]
    #         review_contents=content[1]
            
    #         print title,review_contents

    
    # print author_id,author_name,date,title,review_contents
        

def review_object(author_name,date,title,review_contents):
    review_item={}
    review_item["author_name"]=author_name
    review_item["review_date"]=date
    review_item["review_title"]=title
    review_item["review_contents"]=review_contents
    return review_item


def write_to_json(app_id,review_itemss,num):
    app_review=[]
    app_item={}
    app_item[app_id]=review_itemss
    app_review.append(app_item)
    
    number=1500
    count=0
    exist=False
    position=0
    
    path=str(num)+".json"
    file=open(path)
    fp=json.load(file)
    
    
    for i in range(0,len(fp)):
        map=fp[i]
        if map.has_key(app_id):
            exist=True
            position=i
        for key in map.keys():
            count=count+len(map[key])
                        
    if count+len(review_itemss)>number:
        num=num+1
        path_new=str(num)+".json"
        file_new=open(path_new,"w+")
        
        json.dump(app_review,file_new)
        file_new.close()
    else:
        if exist:
            review_tuple=fp[position][app_id]
            # position
            review_add=review_tuple+review_itemss
            fp[position][app_id]=review_add
            file.close()
            f=open(path,"w+")
            json.dump(fp,f)
            f.close()
        else:
            fp.append(app_item)
            file.close()
            f=open(path,"w+")
            json.dump(fp,f)
            f.close()
    return num
    
    
def write_data(id,page,pageNum,app_id,path_number):
    review_items=generate_data(page)
    author_names=review_items[0]
    dates=review_items[1]
    review_titles=review_items[2]
    review_datas=review_items[3]
    
    reviews=[]
    
    if len(author_names)==len(dates)==len(review_titles)==len(review_datas):
        for item in range(0,len(author_names)):
            review_item=review_object(author_names[item],dates[item],review_titles[item],review_datas[item])
            reviews.append(review_item)
    else:
        return 0
    
    
    # for item in range(0,len(author_names)):
    #     review_item=review_object(author_names[item],dates[item],review_titles[item],review_datas[item])
    #     reviews.append(review_item)
    
    # app_id="com.google.apples"
    # path_num=1
    num=write_to_json(id,reviews,path_number)
    format="%Y-%m-%d %X"
    t=time.strftime(format,time.localtime(time.time()))
    print 'App_id: ',app_id,'  App_name: ',id,"     Page: ",pageNum,'    Finished    ',t
    # review_app(app_id,reviews)
    return num




def get_id(app_path):
    app_id_lists=[]
    file_app=open(app_path)
    for line in file_app:
        app_id_lists.append(line)
    file_app.close()
    return app_id_lists
        
if __name__=='__main__':
    # write_file()
    # id="com.smgstudio.thumbdrift"
    # source_json(id)
    # generate_data()
    # id="com.facebook.katana"
    app_lists=[]
    app_id_path="wangrun"
    app_lists=get_id(app_id_path)
    prior=1
    new=1
    for id in range(0,len(app_lists)):
        new=Get_page(app_lists[id].strip(),id,prior)
        if new==0:
            # new=prior
            pass
        else:
            prior=new
        
    