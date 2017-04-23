# coding=utf-8

import jieba
import jieba.posseg

string="那一天人们终于想起曾经一度被它们所支配的恐惧,以及被囚禁在鸟笼里的屈辱"
seg=jieba.posseg.cut(string)
pos=[]
for i in seg:
    pos.append([i.word,i.flag])
for i in pos:
    print(i[0],'/',i[1],"#")
