# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 06:11:14 2023

@author: wolfg
"""
import numpy as np

Time  = [       61   ,  67 ,    75 ,    71 ]
Distance = [   430 ,  1036 ,  1307 ,  1150 ]

#test
# Time=   [   7 , 15,   30, 10]
# Distance =[  9 , 40 , 200,10]

# dst = np.zeros(Time[0])
# wins=0
# for acc in range(Time[0]):
# #    dst[acc] = 0
#     for t in range(acc):
#         if t+acc < Time[0]:
#             dst[acc] = dst[acc]+acc
#     if dst[acc] > Distance[0]:
#         wins = wins+1
# print(dst)
# #print(max(dst))
# print(wins)


dst = np.zeros(Time[0])
wins=0
for acc in range(Time[0]):
#    dst[acc] = 0
    for t in range(Time[0]-acc):
       dst[acc] = dst[acc]+acc
    if dst[acc] > Distance[0]:
        wins = wins+1
print(dst)
#print(max(dst))
print(wins)


race=3
dst = np.zeros(Time[race])
wins=0
for acc in range(Time[race]):
#    dst[acc] = 0
    for t in range(Time[race]-acc):
       dst[acc] = dst[acc]+acc
    if dst[acc] > Distance[race]:
        wins = wins+1
print(dst)
#print(max(dst))
print(wins)


#sum=0
mult=0
dst = np.zeros(4)
wins = np.zeros(4)
for race in range(4):
#    wins=0
    dst = np.zeros(Time[race])
    for acc in range(Time[race]):
    #    dst[acc] = 0
        for t in range(Time[race]-acc):
#            if t+acc < Time[race]:
            dst[acc] = dst[acc]+acc
        if dst[acc] > Distance[race]:
            wins[race] = wins[race]+1
    print(wins)
#    sum=sum +(max(dst))
#    print(max(dst))
#print (sum)
print(wins[0]*wins[1]*wins[2]*wins[3])