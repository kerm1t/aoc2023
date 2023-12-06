# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 06:11:14 2023

@author: wolfg
"""
import numpy as np

Time  = [       61   ,  67 ,    75 ,    71 ]
Distance = [   430 ,  1036 ,  1307 ,  1150 ]

# test
# Time=   [   7 , 15,   30, 10]
# Distance =[  9 , 40 , 200,10]


race = 3
wins = np.zeros(4)
for race in range(4):
    dst = np.zeros(Time[race])
    for speed in range(Time[race]):
        for t in range(Time[race]-speed):
           dst[speed] = dst[speed]+speed
        if dst[speed] > Distance[race]:
            wins[race] = wins[race]+1
    print(dst)
print(wins)
print(np.prod(wins))

# ~45 mins, rank 11k
# should have used the given examples as test set earlier :-)
# acc is actually speed :-) ... changed it
# use numpy from start