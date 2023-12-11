# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 06:13:07 2023

@author: wolfg
"""
import pprint as pp

f = open("day11_testdata.txt", "r")
f = open("day11_data.txt", "r")

Lines = f.readlines()
u = []
i=0
for line in Lines:
    line = line.replace('\n', '')
    l = [*line]
    u.append(l)
    if not '#' in l:  # empty row --> expand
        u.append(l)   
    i+=1

# print('--')
# pp.pprint(u) --> pprint doesn't work anymore with the big data

# (1) expand --> columns
emptycol=[]
for c in range(len(u[0])):
    sum = 0
    for r in range(len(u)):
        if (u[r][c]) == '#': sum +=1
    if (sum == 0):  # -> expand
        emptycol.append(1)
    else:
        emptycol.append(0)
print("emptycols=",emptycol)

# ---> now create a new array
u_new = []
for r in range(len(u)):
    newrow = []
    for c in range(len(u[0])):
        newrow.append(u[r][c])
        if emptycol[c]==1:
            newrow.append('.')
    u_new.append(newrow)
# pp.pprint(u_new) --> pprint doesn't work anymore with the big data
            
u = u_new # simplify

# (2) find galaxies
g = []
for r in range(len(u)):
    for c in range(len(u[0])):
        if u[r][c] == '#':
            g.append([r,c])
print(g)

# (3) over all pairs --> calc dists
icnt=0
_sum=0
for i in range(len(g)):
    for j in range(i+1,len(g)):
        icnt+=1
        dc = abs(g[j][0]-g[i][0])
        dr = abs(g[j][1]-g[i][1])
#        print (icnt,g[i],g[j],":",dc,dr,"->",dc+dr)            
        _sum += dc+dr
#    print('--')
print("sum:",_sum)

# geil, gleich beim 1. einreichen die richtige zahl!!!