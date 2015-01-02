#!/usr/bin/env python
# coding=utf-8

import math

def instance(lon1, lan1, lon2, lan2):
    Radius = 6371
    du = lambda x:x*math.pi/180.0

    l1 = Radius*math.sin(du(lon1-lon2))
    l2 = Radius*math.sin(du(lan1-lan2))

    l = math.pow(l1**2+l2**2,1/2.0)
    Math.Sqrt(Math.Pow(Math.Sin(a/2),2) + Math.Cos(radLat1)*Math.Cos(radLat2)*Math.Pow(Math.Sin(b/2),2))
