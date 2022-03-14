#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    sum = 0
    quadSize = int(len(matrix)/2)
    # sum 2x2 rows and columns
    for r in range(quadSize):
        for j in range(quadSize):
            p1 = matrix[r][j]
            p2 = matrix[r][j+1]
            p3 = matrix[r+1][j]
            p4 = matrix[r+1][j+1]
            sum += p1 + p2 + p3 + p4
    return sum

    

if __name__ == '__main__':
    q = 1

    for q_itr in range(q):
        n = 2
        matrix = [[1, 2, 3, 4], [3, 4, 5, 6], [5, 6, 7, 8], [7, 8, 9, 10]]
        result = flippingMatrix(matrix)
        print(result)