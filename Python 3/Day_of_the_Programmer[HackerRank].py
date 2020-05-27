#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year < 1918:
        if year % 4 == 0:
            return ('{0}.{1}.{2}'.format('12','09',year))
        else:
            return ('{0}.{1}.{2}'.format('13','09',year))
    elif year == 1918:
        return ('{0}.{1}.{2}'.format('26','09',year))
    else:
        if year % 400 == 0 or (year %4 ==0 and year % 100 !=0):
            return ('{0}.{1}.{2}'.format('12','09',year))
        else:
            return ('{0}.{1}.{2}'.format('13','09',year))




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
