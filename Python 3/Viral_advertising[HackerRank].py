#!/bin/python3

import math

def viralAdvertising(n):
    a = 0
    b = 5
    for _ in range(n):
        a = a + math.floor(b/2)
        b = math.floor(b/2)*3
    return a


if __name__ == '__main__':

    n = int(input())
    result = viralAdvertising(n)
    print(result)
