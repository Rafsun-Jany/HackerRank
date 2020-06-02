def beautifulDays(i, j, k):
    beautiful_days = 0

    for t in range(i,j+1):
        rev = int(str(t)[::-1])
        diff_rev = abs(t-rev)
        if diff_rev % k == 0:
            beautiful_days += 1

    return beautiful_days

if __name__ == '__main__':

    ijk = input().split()
    i = int(ijk[0])
    j = int(ijk[1])
    k = int(ijk[2])
    result = beautifulDays(i, j, k)
    print(result)
