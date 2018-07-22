#!usr/bin/python

n,k=raw_input().split(" ")
n=int(n)
k=int(k)
x=raw_input().split(" ")
x=map(int,x)
x.sort(reverse=True)
print x[k-1]

