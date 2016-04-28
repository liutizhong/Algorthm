# -*- coding: utf-8 -*-
import re
import urllib2

__author__ = 'liutizhong'

#body = '''<script>var context ='/touch';</script>'''
#body = re.sub(r"var context =\'/touch\'", "var context = \'http://m.yougou.com/touch\'", body)
#print body

myUrl = "http://m.yougou.com"
#myUrl = "http://seoul.yougou.com"
response = urllib2.urlopen(myUrl)
the_page = response.read()
#body = re.sub(r"(?<=href=\")/touch", "http://m.yougou.com", the_page)

body = re.sub(r"img src=", "img class=\"SwiperImg\" src=", the_page)
body=body.replace('http://m.yougou.com:80','http://m.yougou.com')
#body = re.sub(r"src=\"/touch/js/index/ygIndex.js\"", "src=\"http://192.168.211.184/img/allTrafficDayReport/ygIndex.js\"", the_page)
#print body
'''
link_list = re.findall(r"<a.+", body)
for url in link_list:
	print url
'''
#link_list = re.findall(r"<a.+", mm)
'''
for url in link_list:
	print url
'''

if "http://m.yougou.com" == myUrl:
	b = re.compile('appType="5" commonId="(.*?)" href=""').findall(body)
	d = re.compile('appType="1003" commonId="(.*?)" href=""').findall(body)
	e = re.compile('appType="1007" commonId="(.*?)" href=""').findall(body)
	f = re.compile('appType="1005" commonId="(.*?)" href=""').findall(body)
	g = re.compile('appType="1006" commonId="(.*?)" href=""').findall(body)
	h = re.compile('appType="1008" commonId="(.*?)" href=""').findall(body)
	i = re.compile('appType="1001" commonId="(.*?)" href=""').findall(body)
	j = re.compile('appType="1024" commonId="(.*?)" href=""').findall(body)
	k = re.compile('appType="1023" commonId="(.*?)" href=""').findall(body)
	l = re.compile('appType="22" commonId="(.*?)" href=""').findall(body)
	m = re.compile('appType="1014" commonId="(.*?)" href=""').findall(body)
	n = re.compile('appType="1015" commonId="(.*?)" href=""').findall(body)
	o = re.compile('appType="1011" commonId="(.*?)" href=""').findall(body)
	img = re.compile('appType="1011" commonId="(.*?)" href=""').findall(body)
#print b
#link_url = "http://m.yougou.com/touch"
#print b
	for commonId in b:
		body = re.sub(r"appType=\"5\" commonId=\""+commonId+"\" href=\"\"", "appType=\"5\" commonId=\""+commonId+"\" href=\"http://m.yougou.com/"+"t-"+commonId+"\"", body)
	for commonId in d:
		body = re.sub(r"appType=\"1003\" commonId=\""+commonId+"\" href=\"\"", "appType=\"1003\" commonId=\""+commonId+"\" href=\"http://m.yougou.com/brand\"", body)
	for commonId in e:
		body = re.sub(r"appType=\"1007\" commonId=\""+commonId+"\" href=\"\"", "appType=\"1007\" commonId=\""+commonId+"\" href=\"http://m.yougou.com/"+"/product.sc?productid="+commonId+"\"", body)
	for commonId in f:
		body = re.sub(r"appType=\"1005\" commonId=\""+commonId+"\" href=\"\"", "appType=\"1005\" commonId=\""+commonId+"\" href=\"http://m.yougou.com/fenlei"+"\"", body)
	for commonId in g:
		body = re.sub(r"appType=\"1006\" commonId=\""+commonId+"\" href=\"\"", "appType=\"1006\" commonId=\""+commonId+"\" href=\"http://m.yougou.com/fenlei"+commonId+"\"", body)
	for commonId in h:
		body = re.sub(r"appType=\"1008\" commonId=\""+commonId+"\" href=\"\"", "appType=\"1008\" commonId=\""+commonId+"\" href=\"http://m.yougou.com/shoppingcart"+"\"", body)
	for commonId in i:
		body = re.sub(r"appType=\"1001\" commonId=\""+commonId+"\" href=\"\"", "appType=\"1001\" commonId=\""+commonId+"\" href=\"http://m.yougou.com/my/listOrderLogistics.sc"+"\"", body)
	for commonId in j:
		body = re.sub(r"appType=\"1024\" commonId=\""+commonId+"\" href=\"\"", "appType=\"1024\" commonId=\""+commonId+"\" href=\"http://m.yougou.com/showChannel.sc?channelId="+commonId+"\"", body)
	for commonId in k:
		body = re.sub(r"appType=\"1023\" commonId=\""+commonId+"\" href=\"\"", "appType=\"1023\" commonId=\""+commonId+"\" href=\"http://m.yougou.com/mc.sc="+"\"", body)
	for commonId in l:
		body = re.sub(r"appType=\"22\" commonId=\""+commonId+"\" href=\"\"", "appType=\"22\" commonId=\""+commonId+"\" href=\"http://m.yougou.com/my/myIndex.sc"+"\"", body)
	for commonId in m:
		body = re.sub(r"appType=\"1014\" commonId=\""+commonId+"\" href=\"\"", "appType=\"1014\" commonId=\""+commonId+"\" href=\"http://m.yougou.com/my/myorderlist.sc"+"\"", body)
	for commonId in n:
		body = re.sub(r"appType=\"1015\" commonId=\""+commonId+"\" href=\"\"", "appType=\"1015\" commonId=\""+commonId+"\" href=\"http://m.yougou.com/my/listMyFavorites.sc"+"\"", body)
	for commonId in o:
		body = re.sub(r"appType=\"1011\" commonId=\""+commonId+"\" href=\"\"", "appType=\"1011\" commonId=\""+commonId+"\" href=\"http://m.yougou.com/my/listOrderLogistics.sc"+"\"", body)


'''
if "seoul.yougou.com"  in "http://seoul.yougou.com/":
	print "seoul.yougou.com do"
	body = re.sub(r"title=\"http://seoul\.yougou\.com/(.*?)shml\"]","title=\"\"", body)
	body = re.sub(r"src=\"//","src=\"http://", body)
#print body
'''
print "---------------------------------------------------"
#link_list = re.findall(r".+.js", body)
link_list = re.findall(r"<a.+", body)
for url in link_list:
	print url

