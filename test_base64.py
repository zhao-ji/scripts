#!/usr/bin/env python
# coding: utf-8

from base64 import b64encode 
from itertools import repeat
from md5 import new
from string import digits, letters
from uuid import uuid4

'''
check the base64 string random
'''

INFO = {k:[0, 0, 0, 0] for k in digits + letters}

UUID4 = uuid4().hex

SHUFFLE_CHARACTER = [
                     'K', 'v', '4', '9', 'h', 'r', '5', 
                     'L', 'F', 'H', 'f', '2', 'S', 's', 
                     'e', 'y', '6', 'c', 'x', 'B', 
                     'W', '3', '7', 'D', 'X', 'i',
                     'k', 'p', 'g', 'q', 'R', 'Y',
                     'u', 'b', 'A', 'G', 'n', 'Z',
                     'J', 'd', 'P', 'V', 'Q', '8',
                     'j', 'z', 'M', 'E', 'C', 'a',
                     'U', 'T', 'm', 'N', 't', 'w',
                    ]

def gen_code():
    return b64encode(uuid4().hex)[:4]

def gen_code_by_md5():
    random_str = new(uuid4().hex + UUID4).hexdigest()
    slice_into_4_part = [random_str[i:i+8] for i in range(4)]
    gen_4_char_position = map(lambda i: int(i, base=16)%56, slice_into_4_part)
    random_char = [SHUFFLE_CHARACTER[i] for i in gen_4_char_position]
    return ''.join(random_char)

def gen_info(code):
    global INFO
    for index, value in enumerate(code):
        INFO[value][index] += 1

def execute(times):
    for _ in repeat(None, times):
        gen_info(gen_code_by_md5())

def display():
    for key, value in INFO.iteritems():
        print ('character:{key} '
               '1:{value[0]} '
               '2:{value[1]} '
               '3:{value[2]} '
               '4:{value[3]} '
               ).format(key=key, value=value)

if __name__ == '__main__':
    execute(20000)
    display()
