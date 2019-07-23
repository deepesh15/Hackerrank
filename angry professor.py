''' this is my test code
n,k = map(int,input().split())
arr_time =[]
arr_time = map(int,input().split())
onTime,Late =0,0
for i in arr_time:
    
    if(i <= 0):
        onTime +=1
    if(i > 0):
        Late += 1

if(onTime < k):
    print("YES")
else:
    print("NO") '''

    #!/bin/python3
    #this is the final submission
import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    onTime,Late =0,0
    for i in a:
    
        if(i <= 0):
            onTime +=1
        if(i > 0):
            Late += 1

    if(onTime < k):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
