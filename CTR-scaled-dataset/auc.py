# -*- coding:utf-8 -*-

'''
Author:Samuel Chan
This file contain code to calculate the auc score.
'''

import sys


def auc(labels, predicted_ctr):
    i_sorted = sorted(range(len(predicted_ctr)), key=lambda i: predicted_ctr[i], reverse=True)
    auc_temp = 0.0
    tp = 0.0
    fp = 0.0
    tp_pre = 0.0
    fp_pre = 0.0
    last_value = predicted_ctr[i_sorted[0]]
    for i in range(len(labels)):
        if labels[i_sorted[i]] > 0:
            tp += 1
        else:
            fp += 1
        if last_value != predicted_ctr[i_sorted[i]]:
            auc_temp += (tp + tp_pre) * (fp - fp_pre) / 2.0
            tp_pre = tp
            fp_pre = fp
            last_value = predicted_ctr[i_sorted[i]]
    auc_temp += (tp + tp_pre) * (fp - fp_pre) / 2.0
    return auc_temp / (tp * fp)


def evaluate(ids, true_values, predicted_values):
    labels = []
    predicted_ctr = []
    for i in range(len(ids)):
        labels.append(int(true_values[i]))
        predicted_ctr.append(float(predicted_values[i]))
    return auc(labels, predicted_ctr)


if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    ids = []
    true_values = []
    predicted_values = []
    for line in f:
        seg = line.strip().split(",")
        ids.append(seg[0])
        true_values.append(seg[1])
        predicted_values.append(seg[2])
    print evaluate(ids, true_values, predicted_values)
