#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print(arr)

    i = n
    j = 0
    while j<len(arr):
        print(arr[i-1] , end ="")
        print(" ", end = "")
        i = i -1
        j = j + 1


