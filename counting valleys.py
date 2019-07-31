n = int(input())
s = str(input().split())
lvl,v=0,0
for i in s:
    if(i == 'U'):
        lvl+=1
    if(i=='D'):
        lvl-=1
    if(lvl == 0 and i=='U'):
        v+=1
print(v)


'''
hackerrank code

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    lvl,v=0,0
    for i in s:
        if(i == 'U'):
            lvl+=1
        if(i=='D'):
            lvl-=1
        if(lvl == 0 and i=='U'):
            v+=1
    return v

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
'''