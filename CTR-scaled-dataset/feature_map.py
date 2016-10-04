# -*- conding:utf-8 -*-

'''
This file contain code to create some feature from the data set and get the global index of each feature.
'''

import sys

file = open(sys.argv[1], "r")
toWrite = open(sys.argv[2], "w+")

feature_map = {}
feature_index = 0


def processIdFeature(prefix, id):
    global feature_map
    global feature_index
    str = prefix + "_" + id
    if str in feature_map:
        return feature_map[str]
    else:
        feature_index = feature_index + 1
        feature_map[str] = feature_index
    return feature_index


def extractFeature(seg):
    list = []
    list.append(processIdFeature("url", seg[1]))
    list.append(processIdFeature("ad", seg[2]))
    list.append(processIdFeature("ader", seg[3]))
    list.append(processIdFeature("depth", seg[4]))
    list.append(processIdFeature("pos", seg[5]))
    list.append(processIdFeature("query", seg[6]))
    list.append(processIdFeature("keyword", seg[7]))
    list.append(processIdFeature("title", seg[8]))
    list.append(processIdFeature("desc", seg[9]))
    list.append(processIdFeature("user", seg[10]))
    return list


def extractFeature2(seg):
    depth = float(seg[4])
    pos = float(seg[5])
    id = int(pos * 10 / depth)
    return processIdFeature("pos_ratio", str(id))


def extractFeature3(seg):
    list = []
    if (len(seg) >= 16):
        str = seg[2] + "_" + seg[15]
        list.append(processIdFeature("user_gender", str))
    return list


def toStr(label, list):
    line = label
    for i in list:
        line = line + "\t" + str(i) + ":1"
    return line


for line in file:
    seg = line.strip().split("\t")
    list = extractFeature(seg)
    list.append(extractFeature2(seg))
    #list.append(extractFeature3(seg))
    toWrite.write(toStr(seg[0], list) + "\n")

toWrite.close()
file.close()
