# -*- coding:utf-8 -*-

from emoji_pinyin_dict import first_dict
import pypinyin


def get_emoji(word, py):
    return first_dict[py][0] if py in first_dict else word


def get_pinyin(word):
    print(word)
    return pypinyin.pinyin(word)


def get_converted(words):
    emojis = []
    pys = get_pinyin(words)
    for py in pys:
        emo = get_emoji(py[0], py[0])
        emojis.append(emo)
    return ''.join(emojis)


def run():
    words = raw_input(u"请输入要转换的字符：").decode('utf-8')
    print(get_converted(words))


if __name__ == '__main__':
    run()


