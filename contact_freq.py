#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:40:49 2019

@author: pczaf
"""

hit = []
file = 'numcont.xvg'
with open(file, 'r') as out:
            for line in out:
                    hit_data = []
                    hit_data = line.split()
                    number = int(hit_data[1])
                    hit.append(number)
j=0
for i in hit:
    if i == 0:
        j=j+1

print ("Missed contact", j,  "times out of", len(hit), "times")

print ("frequency of contact is", ((len(hit)-j)/len(hit))*100, '%')
~                                                                       
