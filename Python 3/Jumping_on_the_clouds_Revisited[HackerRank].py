
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e = 100
    p = 0
    for i in range(len(c)):
        p = p + k
        if p%(len(c)) !=0:
            e -= 1
            if c[p%(len(c))] == 1:
                e -= 2
        else:
            e -= 1
            if c[0] == 0:
                return e
            else:
                return e-2

if __name__ == '__main__':

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c, k)
    print(result)
