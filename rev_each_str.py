#!usr/bin/python

n=raw_input().split(" ")
r=""
for i in n:
    r=r+i[::-1]+" "
print r
