#!usr/bin/python

s=raw_input()
a=[]
for i in range(len(s)):
    if s[i] not in "aeiou":
        a.append(s[i])
print ''.join(a[::-1])        
