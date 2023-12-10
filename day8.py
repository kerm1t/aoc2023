# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 11:18:27 2023

@author: wolfg
"""
import pandas as pd

#dfi = pd.read_csv("day8_inst.txt",sep=" ")
f = open("day8_inst.txt", "r")
instructions = f.read()
df = pd.read_csv("day8_data.txt",sep=" ",header=None, names=["O", "-", "L", "R"])

df["L"] = df["L"].str.replace('(', '')
df["L"] = df["L"].str.replace(',', '')
df["R"] = df["R"].str.replace(')', '')
inst = [*instructions]
#iptr=0
iptr = df.index[df['O'] =="AAA"].tolist()[0]
istep=0
iallstep=0
#for i in inst:
bnotfound = True
while(bnotfound):
#    if i == "L":
# aaaargh    if df["O"][iptr] == "L":
#    if inst[iptr] == "L":
    if df['O'][iptr]=="ZZZ":
        bnotfound=False
        print("win, steps=",iallstep)
    if inst[istep] == "L":
        _next = df["L"][iptr]
    else:
        _next = df["R"][iptr]
    iptr = df.index[df['O'] == _next].tolist()[0]
#    print("%d,%d"%(iallstep,iptr))
#    if iptr==665:
    # if df['O'][iptr]=="ZZZ":
    #     bnotfound=False
    #     print("win")
    istep+=1
    iallstep+=1
#    if istep>283:
# lol
# inst[282]
# Out[176]: 'R'
    if istep>282:
        istep=0
# aaaaahhhh        iallstep+=284, das war saudumm, hab ich erst addiert und dann nochmal iallstep+=1...
#        exit()
#    if iallstep>666:
#        pass        
#        exit()
# ok, also problem 1: ich hab nicht bei AAA angefangen, sondern bei index=0
# problem 2: number too low