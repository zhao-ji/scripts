#!/usr/bin/env python
# code: utf-8

from argparse import ArgumentParser
from os import walk, rename
from urllib import quote, unquote


def gen_utf_8_name(file_name):
    url_str = file_name.lstrip('emoji_').rstrip('.png')
    url_str = unquote(url_str).strip()
    return quote(url_str).replace('%', '') + '.png'


def execute(path):
    for root, dirs, files in walk(path):
        for file_name in files:
            new_file_name = gen_utf_8_name(file_name)
            rename(path + file_name, path + new_file_name)
            print new_file_name + ',',

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--path', '-p', \
            help='input your file path', \
            default='./', type=str)
    arg = parser.parse_args()
    execute(arg.path)
