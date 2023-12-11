# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 11:18:27 2023

@author: wolfg
"""
import pandas as pd

f = open("day8_inst.txt", "r")
instructions = f.read()
df = pd.read_csv("day8_data.txt",sep=" ",header=None, names=["O", "-", "L", "R"])

df["L"] = df["L"].str.replace('(', '')
df["L"] = df["L"].str.replace(',', '')
df["R"] = df["R"].str.replace(')', '')
inst = [*instructions]

iptr = df.index[df['O'] =="AAA"].tolist()[0]
iinst=0
istep=0
bnotfound = True
while(bnotfound):
    if df['O'][iptr]=="ZZZ":
        bnotfound=False
        print("win, steps=",istep)
    if inst[iinst] == "L":
        _next = df["L"][iptr]
    else:
        _next = df["R"][iptr]
    iptr = df.index[df['O'] == _next].tolist()[0]
    iinst+=1
    istep+=1
    if iinst>282: # simply tested #instructions
        iinst=0

# - make a plan first
# - run with the demo data
# - do not reuse variables