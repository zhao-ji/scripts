#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @nightwish

import time
import gevent

''' how many methods of square unlocking ? '''

num = [1,2,3,4,5,6,7,8,9]

'''         [(1,2,3),(3,2,1),(4,5,6),(6,5,4),(7,8,9),(9,8,7),
            (1,4,7),(7,4,1),(2,5,8),(8,5,2),(3,6,9),(9,6,3),
            (1,5,9),(9,5,1),(3,5,7),(7,5,3)]
            禁止的解锁序列（有条件）                            '''

forbiden = {1:{3:2,7:4,9:5},2:{8:5},
            3:{1:2,9:6,7:5},4:{6:5},
            5:{},
            6:{4:5},7:{9:8,1:4,3:5},
            8:{2:5},9:{7:8,3:6,1:5}}

method_num = 0

def first_node():
    global method_num
    for i in num:
        path = [i]
        node = num[:num.index(i)]+num[num.index(i)+1:]
        unlock(node,path,i)

def first_node_():
    global method_num
    threading = []
    for i in num:
        path = [i]
        node = num[:num.index(i)]+num[num.index(i)+1:]
        threading.append(gevent.spawn(unlock,node,path,i))
    gevent.joinall(threading)

def unlock(num,path,i):
    global method_num
    for j in num:
        if j in forbiden[i].keys():
            if forbiden[i][j] in num:continue
        if len(path)<3:
            node = num[:num.index(j)]+num[num.index(j)+1:]
            chain = path+[j]
            unlock(node,chain,j)
        elif len(path)>2 and len(path)<8:
            method_num+=1
            node = num[:num.index(j)]+num[num.index(j)+1:]
            chain = path+[j]
            unlock(node,chain,j)
        elif len(path)==8:
            method_num+=1
        #text = file('/home/nightwish/Music/log.text','a')
        #text.write('num=%s, path=%s, j=%d, method_num=%d \n' %(num,path,j,method_num))
        #text.close()

if __name__ == '__main__':
    start=time.time()
    time_consume=lambda:'total time is %1.5f seconds ' %(time.time()-start)
    first_node()
    print time_consume()
    start=time.time()
    first_node()
    print time_consume()
    print method_num

