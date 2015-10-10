#!/usr/bin/env python
# coding: utf-8
"""
generate the 62 base code
"""

BASE62_NUMBER = []


def base62(number=0):
    if number > 62:
        quotient, remainder = divmod(number, 62)
        BASE62_NUMBER.insert(0, remainder)
        base62(quotient)
    elif number == 62:
        BASE62_NUMBER.insert(0, 0)
        BASE62_NUMBER.insert(0, 1)
    elif number < 62:
        BASE62_NUMBER.insert(0, number)


def change_to_character(item):
    if 0 <= item <= 9:
        return str(item)
    elif 10 <= item <= 35:
        return chr(item + 55)
    elif 36 <= item <= 61:
        return chr(item + 61)


if __name__ == "__main__":
    num = 5023423455467456745532452
    base62(num)
    print "".join(map(change_to_character, BASE62_NUMBER))
