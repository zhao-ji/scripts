#! /usr/bin/env python
# -*- coding=utf-8 -*-
# @nightwish

import sys

''' devid one list to two lists which's subtract is most low
'''

best = 0
result = []

def init(M,N):
    global best
    L = M + N
    L.sort()
    best = sum(L)/2
    return L

def divid(L):
    global result,best
    cache = []
    for i in xrange(2**(len(L)/2)-1,
            2**len(L)-1-2**(len(L)/2)+1+1):
        for j in range(len(L)):
            if (1<<j)&i!=0:
                cache.append(L[j])
            if len(cache)>len(L)/2 \
                    or len(result)!=0 and abs(sum(cache)-best)>result[-1]:
                j = len(L)
                continue
        cache.append(abs(sum(result)-best))
        print cache
        if result==[] or cache[-1]<result[-1] and len(cache)==len(L)/2+1:
            result = cache
        cache = []

if __name__=='__main__':
    M=[1,2]
    N=[2,3]
    divid(init(M,N))
    print result

