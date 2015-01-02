#!/usr/bin/env python
#coding=utf-8
#@nightwish

L=[]

def depower(a,n):
    b = 0
    for i in range(1,n):
        if a**i<20132013 and 20132013<a**(i+1):
            b = i+1
            break
    return b

def bigpower(a,n):
    b = depower(a,n)
    if b == 0:
        L.append({a:n})
    else:
        c = a**b%20132013
        d = n/b
        e = n%b
        print '      '+str(a)+' '+str(e)
        print str(c)+' '+str(d),
        if e == 0:
            bigpower(c,d)
        else:
            L.append({a:e})
            bigpower(c,d)

num = [12,12]
print num[0],num[1],
bigpower(num[0],num[1])

print L

while len(L)>1:
    g = L[0].keys()[0]**L[0].values()[0]*L[1].keys()[0]**L[1].values()[0]%100
    print L[0].keys()[0],L[0].values()[0],L[1].keys()[0],L[1].values()[0]
    del L[0],L[0]
    L.append({g:1})

print L[0].keys()[0]

