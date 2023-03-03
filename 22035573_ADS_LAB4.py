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

print("number of words:", len(all_words))

nchar = 0
for word in all_words:
    nchar = nchar + len(word)
print("number of characters:", nchar)

length = 0
for word in all_words:
    if len(word) > length:       
        length = len(word)
        lword = word
print("The longest word is ", lword, ". It has ", length, " characters.", sep="")
