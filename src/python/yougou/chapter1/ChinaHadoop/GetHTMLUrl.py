import re
import urllib2
from bs4 import BeautifulSoup
__author__ = 'root'

myUrl = "http://m.yougou.com"
response = urllib2.urlopen(myUrl)
the_page = response.read()
#the_page = '"<a href="http://gg/touch></a><a href="/touch/mem/m"> </a>""'
mm = re.sub(r"(?<=href=\")/touch", "http://m.yougou.com", the_page)
#link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", the_page)

#mmm = ''' <iframe id="iFrame3" name="iFrame3" width="100%" scrolling="no" frameborder="0" src='http://qz.yundasys.com:18090/ws/qry1.jsp?wen=1000230708959&key=519488f1f1241a8a71f80fd34e783f2b'> '''
#a = BeautifulSoup(mmm)

#print dict(a.contents[0].attrs)['src']

#html = "<a href='xxx.xxx' title='xxx.xxx.xxx'>sample text1</a>abcdef<a href='xxx.xxx' title='xxx.xxx.xxx'>sample text2</a>"
#result = map(lambda name: re.sub("<a href=.*?>","",name.strip().replace("</a>","")), re.findall("<a href=.*?>.*?</a>",html))
#print result

#link_list = re.findall(r"<a.+",mm)



b = re.compile('commonId="(.*?)" href=""').findall(mm)
link_url = "http://m.yougou.com/touch"
print b
for ll in b:
    mm = re.sub(r"commonId=\""+ll+"\" href=\"\"", "commonId=\""+ll+"\" href=\"http://m.yougou.com/touch/"+"t-"+ll+"\"", mm)

#link_list = re.findall(r"commonId=\"\w+\" href=\"\"", mm)
link_list = re.findall(r"<a.+",mm)
for url in link_list:
    print url

'''
import urllib2
import re

url = 'http://www.sunbloger.com/'

req = urllib2.Request(url)
con = urllib2.urlopen(req)
doc = con.read()
con.close()

links = re.findall(r'href\=\"(http\:\/\/[a-zA-Z0-9\.\/]+)\"', doc)
for a in links:
    print a
'''