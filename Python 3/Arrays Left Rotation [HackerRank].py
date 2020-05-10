def rotLeft(a, d):
    new_array = [0]*(len(a))
    for i in range(len(a) - 1, -1, -1):
        new_array[i - d] = a[i]
    return new_array

if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    result = rotLeft(a, d)
    print(result)
