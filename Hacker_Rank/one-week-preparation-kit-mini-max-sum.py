#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sum_list = []
    for i in range(len(arr)):
            # print everyting except the current element
            sum_list.append(sum(arr) - arr[i])
            print(sum_list)
    print(min(sum_list), max(sum_list))
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]


    miniMaxSum(arr)
