import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    arr_len = len(arr)
    num_ = []
    plus_count = 0
    minus_count = 0
    zero_count = 0
    for i in range(0, len(arr)):  
        if arr[i] > 0: 
            plus_count += 1
        elif arr[i] < 0:
            minus_count += 1
        else:
            zero_count += 1
    print('{0:.6f}'.format(plus_count/arr_len))
    print('{0:.6f}'.format(minus_count/arr_len))
    print('{0:.6f}'.format(zero_count/arr_len))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
