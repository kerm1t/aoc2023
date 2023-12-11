# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 19:50:05 2023

@author: wolfg
"""

# -> complete by recursion

f = open("day9_testdata.txt", "r")
f = open("day9_data.txt", "r")
# s = f.read()
# print(s)
Lines = f.readlines()
 
# def diff(a_i):
#     a_out = []
#     for i in range(len(a_i)-1):
#         d = a_i[i+1]-a_i[i]
# #        print(d)
#         a_out.append(d)
#     return a_out
        
def diff(a_in):
    a_out = []
    for i in range(len(a_in)-1):
        d = a_in[i+1]-a_in[i]
#        print(d)
        a_out.append(d)
    print (a_out)
    if sum(a_out) == 0:
        new = 0
    else:
        new_from_lvl_below = diff(a_out)
#        print("->",new_from_lvl_below)
        new = a_out[len(a_out)-1] + new_from_lvl_below
        print (a_out[len(a_out)-1],"+",new_from_lvl_below)
#        print(new)
    return new


count = 0
_sum = 0
# Strips the newline character
for line in Lines:
    count += 1
#    print("Line{}: {}".format(count, line.strip()))
    a_s = line.split()
#    print (s_n)
    a_i = [int(_sn) for _sn in a_s]
    print (a_i)
    # a_i2 = diff(a_i)
    # print (a_i2)
    # a_i3 = diff(a_i2)
    # print (a_i3)
    # a_i4 = diff(a_i3)
    # print (a_i4)
    # print ('--')
    # while (notnull):
    #     a = diff(a)
    new_from_lvl_below = diff(a_i)
#    print("->",new_from_lvl_below)
    new = a_i[len(a_i)-1] + new_from_lvl_below    
    print (a_i[len(a_i)-1],"+",new_from_lvl_below)
    print("_________",new)
    _sum += new
print ("sum: ",_sum)    