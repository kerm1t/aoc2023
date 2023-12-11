# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 06:13:07 2023

@author: wolfg
"""
import pprint as pp

f = open("day11_testdata.txt", "r")
f = open("day11_data.txt", "r")
# s = f.read()
# print(s)
Lines = f.readlines()
u = []
i=0
for line in Lines:
    line = line.replace('\n', '')
    l = [*line]
    print(l)
    u.append(l)
    if not '#' in l:  # empty row --> expand
        u.append(l)   
    i+=1

print('--')
pp.pprint(u)

# expand --> columns

# sum = 0
# for i in range(len(u)):
# #    print(i)
#     print(u[i][0]) # over all rows
#     if (u[i][0]) == '#': sum +=1
# if (sum == 0):
#     # -> expand
#     pass
# print(sum)

emptycol=[]
for c in range(len(u[0])):
    sum = 0
    for r in range(len(u)):
    #    print(i)
        # print(u[r][c]) # over all rows
        if (u[r][c]) == '#': sum +=1
    if (sum == 0):
        # -> expand
        emptycol.append(1)
    else:
        emptycol.append(0)
    # print(sum)            
print("emptycols=",emptycol)

u_new = []
for r in range(len(u)):
    newrow = []
    for c in range(len(u[0])):
        newrow.append(u[r][c])
        if emptycol[c]==1:
            newrow.append('.')
    u_new.append(newrow)
pp.pprint(u_new)
            
u = u_new # simplify

# find pairs
g = [] # galaxies
for r in range(len(u)):
    for c in range(len(u[0])):
        if u[r][c] == '#':
            g.append([r,c])
print(g)
# for _g in g:
#     for _g2 in g:
#         if (_g is not _g2):
#             print (_g,_g2)
#     print('--')


# calc dists
# for _g in g:
#     for _g2 in g:
#         if (_g is not _g2):
#             # print (_g,_g2)
#             # print(_g[0])
#             dc = abs(_g2[0]-_g[0])
#             dr = abs(_g2[1]-_g[1])
#             # print(dc)
#             print (_g,_g2,":",dc,dr,"->",dc+dr)            
#     print('--')

icnt=0
_sum=0
for i in range(len(g)):
    for j in range(i+1,len(g)):
        icnt+=1
#        if (_g is not _g2):
        # print (_g,_g2)
        # print(_g[0])
        dc = abs(g[j][0]-g[i][0])
        dr = abs(g[j][1]-g[i][1])
        # print(dc)
        print (icnt,g[i],g[j],":",dc,dr,"->",dc+dr)            
        _sum += dc+dr
    print('--')
print("sum:",_sum)

# geil, gleich beim 1. einreichen die richtige zahl!!!