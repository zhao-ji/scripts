#!/usr/bin/env python
#-*- coding=utf-8 -*-
# @nightwish

''' eight queens question '''

m = [0,1,2,3,4,5,6,7]
n = [0,1,2,3,4,5,6,7]
solution = []
node = []

def queens():
    global list
    for i in m[0:1]:
        for j in n:
            new_node = node+[(i,j)]
            new_m = m[:m.index(i)]+m[m.index(i)+1:]
            new_n = n[:n.index(j)]+n[n.index(j)+1:]
            next(new_m,new_n,new_node)

def next(m,n,node):
    for i in m:
        for j in n:
            if all(not(i-k[0]==j-k[1] or i-k[0]==k[1]-j) for k in node):
                new_node = node+[(i,j)]
                new_m = m[:m.index(i)]+m[m.index(i)+1:]
                new_n = n[:n.index(j)]+n[n.index(j)+1:]
                if len(new_node)==8:
                    new_node.sort()
                    if new_node not in solution:
                        solution.append(new_node)
                        print new_node
                else:
                    next(new_m,new_n,new_node)
            else:
                continue
if __name__ == '__main__':
    queens()
    print len(solution)
