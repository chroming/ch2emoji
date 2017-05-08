# -*- coding:utf-8 -*-

from emoji_pinyin_dict import first_dict, all_dict
import pypinyin
import random


def get_emoji(word, py):
    return first_dict[py][0] if py in first_dict else word


def get_random_emoji(word, py):
    return random.sample(all_dict[py], 1)[0] if py in all_dict else word


METHOD = {
    0: get_emoji,
    1: get_random_emoji
}


def get_pinyin(word):
    print(word)
    return pypinyin.pinyin(word)


def get_converted(words, method=0):
    emojis = []
    pys = get_pinyin(words)
    for py in pys:
        emo = METHOD[method](py[0], py[0])
        emojis.append(emo)
    return ''.join(emojis)


def run(method=0):
    words = raw_input("Please input text: ").decode('utf-8')
    print(get_converted(words, method))


if __name__ == '__main__':
    run(1)


