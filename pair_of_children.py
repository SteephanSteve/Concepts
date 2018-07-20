#!usr/bin/python

n=int(input())
p=0
for i in range(n):
    for j in range(i+1,n):
        if i<=2*n-1:
            p+=1
print p



