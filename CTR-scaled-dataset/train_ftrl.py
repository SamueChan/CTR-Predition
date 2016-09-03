# -*- coding:utf-8 -*-

'''
Author:Samuel Chan
This file contain code to train the model with logistic regression and FTRL.
'''

import random
import math

alpha = 0.5
l2 = 10
l1 = 0.1
beta = 0.01
iter = 2

file = open("train_feature", "r")
max_index = 0
for f in file:
    seg = f.strip().split("\t")
    for st in seg[1:]:
        index = int(st.split(":")[0])
        if index > max_index:
            max_index = index

w = range(max_index + 1)
z = range(max_index + 1)
n = range(max_index + 1)

for i in range(max_index + 1):
    w[i] = random.uniform(-0.5, 0.5)
    z[i] = 0
    n[i] = 0

for i in range(iter):
    file = open("train_feature", "r")
    for f in file:
        seg = f.strip().split("\t")
        label = int(seg[0])
        s = 0.0
        for st in seg[1:]:
            index = int(st.split(":")[0])
            s += w[index]
        p = 1.0 / (1 + math.exp(-s))
        g = p - label
        for st in seg[1:]:
            index = int(st.split(":")[0])
            sigma = (math.sqrt(n[index] + g * g) - math.sqrt(n[index])) / alpha
            z[index] = z[index] + g - sigma * w[index]
            n[index] = n[index] + g * g
            if math.fabs(z[index]) < l1:
                w[index] = 0
            else:
                if z[index] > 0:
                    w[index] = -(z[index] - l1) / ((beta + math.sqrt(n[index])) / alpha + l2)
                else:
                    w[index] = -(z[index] + l1) / ((beta + math.sqrt(n[index])) / alpha + l2)

file = open("validata_feature", "r")
toWrite = open("pctr", "w+")
c = 0
for f in file:
    c += 1
    seg = f.strip().split("\t")
    label = int(seg[0])
    s = 0.0
    for st in seg[1:]:
        index = int(st.split(":")[0])
        if index <= max_index:
            s += w[index]
    p = 1.0 / (1 + math.exp(-s))
    s = str(c) + "," + seg[0] + "," + str(p) + "\n"
    toWrite.write(s)

toWrite.close()

c = 0
filet = open("test_feature", "r")
toWrite2 = open("test_pctr", "w+")
toWrite3 = open("test_pctr.csv", "w+")
for f in filet:
    c += 1
    seg = f.strip().split("\t")
    s2 = 0.0
    for st in seg[1:]:
        index = int(st.split(":")[0])
        if index <= max_index:
            s2 += w[index]
    p = 1.0 / (1 + math.exp(-s2))
    label = 0
    if p > 0.5:
        label = 1
    s2 = str(c) + "," + str(label) + "," + str(p) + "\n"
    s3 = str(p) + "\n"
    toWrite2.write(s2)
    toWrite3.write(s3)

toWrite2.close()
toWrite3.close()
