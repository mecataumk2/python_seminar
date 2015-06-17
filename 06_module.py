__author__ = 'sdlee'

f = open("sample.txt", 'r')
for line in f.readlines():
    print line.strip()

f.close()
