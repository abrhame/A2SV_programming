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
    # take the first element and store it in a variable
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        # compare the key with all elments that are greater than the key and  also shift the other elments in the place of key and the key is greater than others insert the key at that index
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            # print all the elemnts of the array
            for i in arr:
                print(i,end = " ")
            print() # used as a new line
        arr[j+1] = key
    
    # print all the elemnts of the array
    for i in arr:
        print(i,end = " ")
        

            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
