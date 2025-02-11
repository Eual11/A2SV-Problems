# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    i = n-1 
    for j in range(1, (n)):
            x = arr[i]
            j =i 
            
            while j >=1 and arr[j-1] > x:
                arr[j] = arr[j-1]
                print(" ".join([str(i) for i in arr]))
                       
                j-=1
            arr[j] = x
    print(" ".join([str(i) for i in arr]))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
