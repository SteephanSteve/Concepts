#!usr/bin/python

l=int(input())
r=int(input())
c=0
for n in range(l,r+1):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print n
            c+=1
print c
