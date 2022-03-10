#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Write your code here
    arr_len = len(arr)
    if arr_len % 2 == 0:
        if arr_len % 2 != 0:
            return (arr[arr_len//2]) - 1
        else:
            return ((arr[arr_len//2] + arr[arr_len//2 - 1])//2) -1
    else:
        return (arr[arr_len//2]) - 1

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(findMedian(arr))
