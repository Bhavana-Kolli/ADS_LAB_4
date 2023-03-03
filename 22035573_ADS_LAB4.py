#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 17:41:12 2023

@author: kollibhavana
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import clean_up as cl

text = open("big_data.txt", "r")
all_words = []
counter = 0
for line in text:   
    words = line.split()
    counter = counter + 1
    for word in words:        
        word = cl.clean(word)
        all_words.append(word)
print(all_words)
df_words = pd.DataFrame(data=all_words, columns=("words",))
df_counts = df_words["words"].value_counts()

df_counts.to_csv("wordcount.csv")

print(len(df_counts))
print(df_counts)
print(df_counts.iloc[100:120])