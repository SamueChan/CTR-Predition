# -*- conding:utf-8 -*-

'''
Author:Samuel Chan
This file contain code to train the model with logistic regression and SGD.
'''

import math
import random

alpha = 0.1
iter = 1
l2 = 1

file = open("train_feature", "r")

max_index = 0

for f in file:
    seg = f.strip().split("\t")
    for st in seg[1:]:
        index = int(st.split(":")[0])
        if index > max_index:
            max_index = index

weight = range(max_index + 1)

for i in range(max_index + 1):
    weight[i] = random.uniform(-0.01, 0.01)

for i in range(iter):
    file = open("train_feature", "r")
    for f in file:
        seg = f.strip().split("\t")
        label = int(seg[0])
        s = 0.0
        for st in seg[1:]:
            index = int(st.split(":")[0])
            s += weight[index]
        p = 1.0 / (1 + math.exp((-s)))
        g = p - label
        for st in seg[1:]:
            weight[index] -= alpha * (g + weight[index])

file = open("validate_feature", "r")
toWrite = open("pctr", "w+")
for f in file:
    seg = f.strip().split("\t")
    label = int(seg[0])
    s = 0.0
    for st in seg[1:]:
        index = int(st.split(":")[0])
        s += weight[index]
    p = 1.0 / (1 + math.exp(-s))
    s = seg[0] + "," + str(p) + "\n"
    toWrite.write(s)

toWrite.close()
