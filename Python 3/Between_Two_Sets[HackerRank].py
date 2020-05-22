#!/bin/python3

from math import gcd

def getTotalX(a, b):
    c=[0]*len(b)
    count = 0
    for i in range(len(b)):
        c[i] = [t for t in range(a[len(a)-1],b[i]+1) if b[i]%t==0]

    d = set(c[0])
    for i in range(1,len(c)):
        d = d.intersection(set(c[i]))
    d = list(d)
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm*i//gcd(lcm,i)

    for i in d:
        if i%lcm == 0:
            count +=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
