b,n,m = list(map(int,input().split()))
keyboards = list(map(int,input().split()))
USBs =list(map(int,input().split()))
sums = []
for e in keyboards:
    for i in USBs:
        if( e+i < b or e+i == b):
            sums.append(e+i)
print(max(sums))


'''
hackerrank code

#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    sums = []
    for e in keyboards:
        for i in drives:
            if( e+i < b or e+i == b):
                sums.append(e+i)
    try:
        return  max(sums)
    except ValueError as err:
        return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
'''

'''
really cools solution

#!/bin/python3
from itertools import product

def getMoneySpent(K, D, s):
    return max((k+d if k+d<=s else -1 for k,d in product(K,D)))
    '''