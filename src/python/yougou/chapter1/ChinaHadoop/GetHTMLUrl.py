import re
import urllib2
__author__ = 'root'

myUrl = "http://m.yougou.com"
#response = urllib2.urlopen(myUrl)
#the_page = response.read()
the_page = '"<a href="http://gg/touch></a><a href="/touch/mem/m"> </a>""'
mm = re.sub(r"(?<=href=\")/touch", "http://m.yougou.com", the_page)
#link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", the_page)
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