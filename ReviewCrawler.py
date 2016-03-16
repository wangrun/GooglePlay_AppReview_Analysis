import urllib,urllib2


url="https://play.google.com/store/getreviews?authuser=0"
count=2
values={}
values['reviewType']='0'
values['pageNum']=str(count)
values['id']='com.facebook.katana'
values['reviewSortOrder']='2'
values['xhr']='1'
values['hl']='en'

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36','Referer':'https://play.google.com/store/apps/details?id=com.facebook.katana&hl=en','Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}

proxy = '127.0.0.1:8787'
opener = urllib2.build_opener(urllib2.ProxyHandler({'https':proxy}))
urllib2.install_opener(opener)


data=urllib.urlencode(values)
request=urllib2.Request(url,data,headers)
page=""

while 1:
    response=urllib2.urlopen(request)
    page=response.read()
    print page
    count=count+1
    break

start=page.index("<div")
end=page.rindex("</div>")
comments=page[start:end]
com_text=comments
com_text = com_text.replace('\u003c', '<')
com_text = com_text.replace('\u003e', '>')
com_text = com_text.replace('\u003d', '=')
com_text = com_text.replace('\u003a', ':')
com_text = com_text.replace('\u0026', '&')
com_text = com_text.replace('\"', '"')
com_text = com_text.replace('\\n"', '\n')

# comm = unicode(str(comments), 'utf-8')
soup=BeautifulSoup(com_text)
print soup.text



# com_text=page
# com_text = com_text.replace('\u003c', '<')
# com_text = com_text.replace('\u003e', '>')
# com_text = com_text.replace('\u003d', '=')
# com_text = com_text.replace('\u003a', ':')
# com_text = com_text.replace('\u0026', '&')
# com_text = com_text.replace('\"', '"')
# com_text = com_text.replace('\\n"', '\n')
# print com_text




    
