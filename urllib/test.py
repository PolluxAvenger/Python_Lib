# coding=utf-8

import urllib.parse

if __name__ == '__main__':
    word = '中国'
    word_url = urllib.parse.quote(word)
    print(word_url)
