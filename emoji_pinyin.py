# -*- coding:utf-8 -*-

from emoji_dict import emoji_dict
import pypinyin


py_dict = {pypinyin.pinyin(key, heteronym=True)[0][0]:values for key, values in emoji_dict.iteritems()}
print py_dict


