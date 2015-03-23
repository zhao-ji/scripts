#!/usr/bin/env python
# coding: utf8

PIXLE = set()

def get_pos(x):
    global PIXLE

    y = (50 ** 2 - x ** 2) ** (float(1) / 2)
    print "the X is {}, the Y is {}".format(x, y)

    if y != int(y):
        coord_1 = (x, int(y))
        coord_2 = (x - 1, int(y))
        print "cross {}, {}".format(coord_1, coord_2)
        PIXLE.add(coord_1)
        PIXLE.add(coord_2)
    else:
        coord_1 = (x, y)
        coord_2 = (x - 1, y)
        coord_3 = (x, y - 1)
        coord_4 = (x - 1, y - 1)
        print "cross {}, {}, {}, {}".format(coord_1, coord_2, coord_3, coord_4)
        PIXLE.add(coord_1)
        PIXLE.add(coord_2)
        PIXLE.add(coord_3)
        PIXLE.add(coord_4)


if __name__ == "__main__":
    for x in range(50, -1, -1):
        get_pos(x)
    print "the length of PIXLE is {}".format(len(PIXLE))
    # f = open("pixle.txt", "w")
    # f.write(PIXLE)
