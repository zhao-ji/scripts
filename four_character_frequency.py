#!/usr/bin/env python
# coding: utf-8

import sys

FOUR_CHARACTER_FREQUENCY = {}

if __name__ == "__main__":
    # 原始文本默认utf-8编码
    for line in sys.stdin:
        # 按标点符号和空格划分句子
        sentence_list = line.split(" ")
        for split_string in [",", ".", "?", "!", "，", "。"]:
            sentence_list = map(
                lambda sentence: getattr(sentence, "split")(split_string),
                sentence_list,
            )
            sentence_list = reduce(
                lambda i, j: i + j,
                sentence_list,
                [],
            )
        # 移除空句子
        sentence_list = filter(None, sentence_list)
        # 每个句子汉字长度大于3
        sentence_list = filter(
            lambda sentence: len(sentence.decode("utf8")) > 3,
            sentence_list,
        )
        # 转为unicode编码
        for sentence in sentence_list:
            sentence = sentence.decode("utf-8")
            sentence_length = len(sentence)
            # 把每一个四字词放入统计字典 频数加一
            for anchor in range(sentence_length - 3):
                FOUR_CHARACTER_FREQUENCY[
                    sentence[anchor:anchor+4]
                ] = FOUR_CHARACTER_FREQUENCY.setdefault(
                    sentence[anchor:anchor+4], 0
                ) + 1
    # 把所有频数统计打印出来
    for four_character in FOUR_CHARACTER_FREQUENCY:
        print FOUR_CHARACTER_FREQUENCY.get(four_character), \
            four_character.encode("utf-8")
