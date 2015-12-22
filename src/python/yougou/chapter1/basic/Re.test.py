import re
a = '<area shape="rect" coords="157,804,323,848" href="#" />'
b = re.compile('rect" coords="(.*?)" href="#" ').findall(a)[0]
#c = b.findall(a)[0]
print b
d = b.split(",")
A = d[0]
B = d[1]
C = d[2]
D = d[3]
print A, B, C, D

ptn = re.compile(".+coords=\"([\d,]+)\".+")
result = ptn.match(a)
arr = result.group(1).split(",")
print arr[0], arr[1], arr[2], arr[3]