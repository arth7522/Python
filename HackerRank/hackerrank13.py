import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    sum1=0
    for x in range(len(arr)):
        sum1+=int(arr[x][x])

    sum2=0
    y=int((len(arr))-1)
    for x in range(len(arr)):
        sum2+=int(arr[x][y])
        y-=1
    ans=abs(sum1-sum2)
    return ans

n = int(input())

arr = []

for _ in range(n):
    arr.append(input().split())



result = diagonalDifference(arr)
    #fptr.write(str(result) + '\n')
print(result)
    #fptr.close()
