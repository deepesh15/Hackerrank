n,d = list(map(int,input().split()))
arr = list(map(int,input().split()))
count =0
for i in range(n):
    if arr[i]+d in arr and arr[i]+2*d in arr :
        count+=1
print(count)



'''
hackerrank code
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    count=0
    for i in range(len(arr)):
        if arr[i]+d in arr and arr[i]+2*d in arr :
            count+=1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
'''