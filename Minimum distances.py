n = int(input())
a  = list(map(int,input().split()))
dist =[]
for i in a:
    indices = [j for j,x in enumerate(a) if x==i]
    try:
        dist.append(abs(indices[0]-indices[1]))
    except IndexError as error:
        continue


print(min(dist))



'''
# hackerrank code
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    dist =[]
    for i in a:
        indices = [j for j,x in enumerate(a) if x==i]
        try:
            dist.append(abs(indices[0]-indices[1]))
        except IndexError as error:
            continue
    try:
        return min(dist)
    except ValueError as err:
        return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
'''