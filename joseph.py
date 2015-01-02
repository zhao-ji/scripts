#!/usr/bin/env python
#-*- coding=utf-8 -*-
# @nightwish

'''
   约瑟夫环
'''

def joseph(n,k,m):
    '''
        输入 人数、起始位置、第几人出列
        输出 出列顺序的列表
    '''
    L1 = []
    for i in range(1,n+1):
        L1.append(i)
    L2 = []
    while len(L1)>1:
        L1 = L1 + L1[0:k-1]
        del L1[0:k-1]
        print L1
        l = m%len(L1)
        L2.append(L1[l-1])
        print L2
        del L1[l-1]
        k = l
    L2.append(L1[0])
    print L2
