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
# def cards_sort(hand):
#     return hand
# ... not needed (s. rules :-)
print(_order)

def dec2hex(dec):
    return hex(dec).split('x')[-1]

def camel_score(hand): # e.g. "2" gets score 0, "T" gets a score of 8
    global _rorder
    cards = [*hand]
    print(cards)
    # i = 0
    # vals = [0,0,0,0,0]
    # for c in cards:
    #     for o in order:
    #         if c == o:
    #             vals[i] = 
    vals = [0,0,0,0,0]
    vals[0] = _rorder.index(cards[0])
    vals[1] = _rorder.index(cards[1])
    vals[2] = _rorder.index(cards[2])
    vals[3] = _rorder.index(cards[3])
    vals[4] = _rorder.index(cards[4])
    print ("cmelscore = ",vals)
    # score = 10000*hex(vals[0])
    # score += 1000*hex(vals[1])
    # score += 100*hex(vals[2])
    # score += 10*hex(vals[3])
    # score += hex(vals[4])
    # print ("camelscore = ",score)
    cs = str(dec2hex(_rorder.index(cards[0])))
    cs += str(dec2hex(_rorder.index(cards[1])))
    cs += str(dec2hex(_rorder.index(cards[2])))
    cs += str(dec2hex(_rorder.index(cards[3])))
    cs += str(dec2hex(_rorder.index(cards[4])))
#    return vals
#    cs = 
    print(cs)
    return cs # camel score
    
def poker_score(hand):
    cards = [*hand]
    print(cards)
    d = ["","","","",""]
    n = [0,0,0,0,0]
#     for i in range(5):
#         if cards[i] in d:
# #            n[i]+=1
#             n[d.index(cards[i])]+=1
#         else:
#             d[i] = cards[i]                                  
#             n[i]+=1
    i_d = 0
    for c in cards:
        if c in d:
            n[d.index(c)]+=1
        else:
            d[i_d] = c                                  
            n[i_d]+=1
            i_d+=1
    # sort first ... not needed ... now, but later when comparing hands
#    if 1 in n: s = 1
    # s = 1
    # if 5 in n: s = s+64
    # if 4 in n: s = s+32
    # if (3 in n):
    #     if (2 in n):
    #         s = s+16
    #     else:
    #         s = s+8
    # if 2 in n:
    #     s = s+16
    # tut so nicht, weil berücksichtigt keine two pairs
    
    # 7 types of cards
    # pairing = [0,0,0,0,0]
    # for m in n:
    #     if m = 5:
    #         pairing[5-1] = 1  
    #     if m = 4:
    #         pairing[4-1] = 1  
    #     if m = 3:
    #         pairing[3-1] = 1  
    #     if m = 2:
    #         pairing[3-1] +=1
    #    
    # if pairing[5-1] == 1: s = 64
    # if pairing[4-1] == 1: s = 32
    # if (3 in n):
    #     if (2 in n):
    #         s = s+16
    #     else:
    #         s = s+8
    # if 2 in n:
    #     s = s+16
    # zu aufwändig ...

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
    print(d)
    print(n)
    print("score = ",s)
    return s


def sort_poker_val(df):
    pass


#df = pd.read_csv("test_day7.txt",sep=" ")
df = pd.read_csv("data_day7.txt",sep=" ")
ps = []
cs = []
for ind in df.index:
    print(df['hand'][ind], df['bid'][ind])
# ok, after all this implementation thinking of the algo now
# - map cards to numbers "A" = 12, "2" = 0
# 
    # ps = poker_score(df['hand'][ind])
    # cs = camel_score(df['hand'][ind])
    # df['ps'][ind] = ps
    # df['cs'][ind] = cs
    
    ps.append(poker_score(df['hand'][ind])) # not push_back :-)
    cs.append(camel_score(df['hand'][ind]))

df['ps'] = ps
df['cs'] = cs

df2 = df.sort_values(['ps', 'cs'], ascending = [True, True])

# winnings = 0
# for ind in df2.index:
#     print(df2['bid'][ind])
#     win = (ind+1) * df2['bid'][ind]
#     print(win)
#     winnings += (ind+1) * df2['bid'][ind]
# print(winnings)
# index is scrambled after sorting

df2 = df2.reset_index(drop=True)

# winnings = 0
# for ind in df2.index:
# #    print(df2['bid'][ind])
#     win = (ind+1) * df2['bid'][ind]
#     print("win: ", win)
#     winnings += (ind+1) * df2['bid'][ind]
# print(winnings)

# Houston, we have a problem

winnings = []
for ind in df2.index:
    win = (ind+1) * df2['bid'][ind]
    winnings.append((ind+1) * df2['bid'][ind])

df2["winnings"] = winnings
print("sum --> ",df2["winnings"].sum())
###, stimmt nicht,
# ok, ich habe noch einen bug gefunden,
# poker_score("22777")
# ['2', '2', '7', '7', '7']
# ['2', '7', '', '', '']
# [2, 3, 0, 0, 0]
# score =  2
 