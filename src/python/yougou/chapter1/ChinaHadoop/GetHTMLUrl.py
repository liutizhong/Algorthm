# -*- coding: utf-8 -*-
import re
import urllib2
__author__ = 'root'

myUrl = "http://m.yougou.com/touch"
req_header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

req = urllib2.Request(myUrl, None, req_header)
page = urllib2.urlopen(req)

#response = urllib2.urlopen(myUrl)
the_page = page.read()
the_page = the_page.decode('UTF-8')
page.close()
print the_page
#the_page = '"<a href="http://gg/touch></a><a href="/touch/mem/m"> </a>""'
mm = re.sub(r"(?<=href=\")/touch", "http://m.yougou.com", the_page)

mms =re.sub(r"<a.+ ")

#link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", the_page)
link_list = re.findall(r"<a.+", mm)
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