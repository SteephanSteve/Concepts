#!usr/bin/python

a=int(input())
b=[]
c=0
for i in range(a):
    d=a%10
    b.append(d)
    a=a//10
    if a==0:
        break
for i in range(len(b)):
    c=c+b[i]*b[i]
print c

