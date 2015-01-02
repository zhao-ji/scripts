#!/usr/bin/env python
#-*- coding=utf-8 -*-

def bigmod(a,n,d):
    res = 1
    while n>1:
        if n%2 == 1:
            res = a*res%d
        a = a**2%d
        n>>=1
    return res*a%d
    
