#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[-2::] == "AM":
        if int(s[0:2]) >= 12:
            return "0"+str(int(s[0:2]) - 12) + s[2:-2]
        else:
            return s[0:-2]
    elif s[-2::] == "PM":
        if int(s[0:2]) < 12:
            return str(int(s[0:2]) + 12) + s[2:-2]
        else:
            return s[0:-2]


if __name__ == '__main__':

    s = "17:05:45AM"

    print(timeConversion(s))

