import sys
from collections import Counter
__author__ = 'root'

try:
    num_words = int(sys.argv[1])
    print sys.argv[1]
except:
    print "usage: most_commom_words.py num_words"
    sys.exit(1)
counter = Counter(word.lower()
                  for line in sys.stdin
                  for word in line.strip().split()
                  if word)
for word,count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")



#file_for_reading = open('/usr/temp/1.txt','r')

# cat /usr/temp/1.txt | python most_common_word.py 10  