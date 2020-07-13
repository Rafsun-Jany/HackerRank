def minimumDistances(a):
    distances = []
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i] == a[j]:
                d = abs(i-j)
                distances.append(d)
    if len(distances) == 0:
        return -1
    else:
        return min(distances)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
