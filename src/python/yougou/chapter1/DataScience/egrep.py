import sys,re
__author__ = 'root'

regex = sys.argv[1]
for line in sys.stdin:
    if re.search(regex,line):
        sys.stdout.write(line)



