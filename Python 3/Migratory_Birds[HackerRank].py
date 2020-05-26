#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    birds_dict = {}
    for i in arr:
        if i in birds_dict:
            birds_dict[i] +=1
        else:
            birds_dict[i] = 1
    max_val = birds_dict.values()
    max_val = max(max_val)
    max_arr = []
    for i in birds_dict:
        if birds_dict[i] == max_val:
            max_arr.append(i)
    max_arr.sort()
    return max_arr[0]

if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    print(result)
