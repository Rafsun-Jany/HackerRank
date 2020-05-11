""""
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    my_number = int(input().strip())
    if my_number % 2 == 0 and (2 <= my_number <= 5):
        print("Not Weird")
    elif my_number % 2 == 0 and (6 <= my_number <= 20):
        print("Wired")
    elif my_number % 2 == 0 and my_number > 20:
        print("Not Wired")
    else:
        if my_number % 2 != 0:
            print("Wired")

"""
if __name__ == '__main__':
    N = int(input())
    if N % 2 != 0:
        print("Weird")
    else:
        if 2 <= N <= 5:
            print("Not Weird")
        elif 6 <= N <= 20:
            print("Weird")
        elif N > 20:
            print("Not Weird")
