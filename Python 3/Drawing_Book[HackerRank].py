
# Complete the pageCount function below.
#
def pageCount(n, p):
    n_avg = n//2
    if p <= n_avg:
        return p//2
    else:
        return abs(n_avg-(p//2))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    p = int(input())
    result = pageCount(n, p)
    fptr.write(str(result) + '\n')
    fptr.close()
