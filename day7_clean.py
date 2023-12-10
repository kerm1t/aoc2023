# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 07:51:49 2023

@author: wolfg
"""

import pandas as pd
import string as st

_order =  ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]    
_order.reverse()
_rorder = _order
print(_rorder)

def dec2hex(dec):
    return hex(dec).split('x')[-1]

def camel_score(cards): # e.g. "2" gets score 0, "T" gets a score of 8
    cs = str(dec2hex(_rorder.index(cards[0])))
    cs += str(dec2hex(_rorder.index(cards[1])))
    cs += str(dec2hex(_rorder.index(cards[2])))
    cs += str(dec2hex(_rorder.index(cards[3])))
    cs += str(dec2hex(_rorder.index(cards[4])))
    return cs # camel score
    
def poker_score(cards):
    d = ["","","","",""]
    n = [0,0,0,0,0]
    i_d = 0
    for c in cards:
        if c in d:
            n[d.index(c)]+=1
        else:
            d[i_d] = c                                  
            n[i_d]+=1
            i_d+=1
    s = 1
    if 5 in n: s = 64
    if 4 in n: s = 32
    if (3 in n):
        if (2 in n):
            s = 16
        else:
            s = 8
    else: # das hatte gefehlt, dadurch wurde full house durch 2 überschrieben
        if 2 in n:
            ntwo = 0
            for m in n:
                if m == 2:
                    ntwo += 1
            if ntwo == 2:
                s = 4
            else:
                s = 2
    return s


#df = pd.read_csv("test_day7.txt",sep=" ") # <-- helpful
df = pd.read_csv("data_day7.txt",sep=" ")
ps = []
cs = []
for ind in df.index:
    hand = df['hand'][ind]
    cards = [*hand]
    ps.append(poker_score(cards)) # not push_back :-)
    cs.append(camel_score(cards))

df['ps'] = ps
df['cs'] = cs
df2 = df.sort_values(['ps', 'cs'], ascending = [True, True]) # i.e. sort by "rank"
df2 = df2.reset_index(drop=True)

winnings = []
for ind in df2.index:
    win = (ind+1) * df2['bid'][ind]
    winnings.append((ind+1) * df2['bid'][ind])

df2["winnings"] = winnings
print("sum --> ",df2["winnings"].sum())
