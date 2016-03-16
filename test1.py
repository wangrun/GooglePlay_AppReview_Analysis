import urllib
import urllib2
import cookielib

proxy = '127.0.0.1:8787'

cookie=cookielib.LWPCookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(urllib2.ProxyHandler({'https':proxy}),handler)
urllib2.install_opener(opener)
response=opener.open('https://play.google.com/store/apps/details?id=com.facebook.katana&hl=en')

for item in cookie:
    print item.name,item.value
