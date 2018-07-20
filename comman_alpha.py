#!usr/bin/python


n=int(input())
a=[]
b=[]
c=0
for i in range(n):
    s=raw_input()
    a.append(s)
for j in range(len(min(a))):
    for i in range(n):
        if i<n-1:
            if a[i][j]==a[i+1][j]:
               c+=1
            i-=1
    if c==n-1:
         b.append(a[i][j])
    else:
         break
    c=0                    
if b:
    print ''.join(b)
else:
    print "No matches"
