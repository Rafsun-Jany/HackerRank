from itertools import permutations
def formingMagicSquare(s):
    minimum_cost = None
    d = []
    n = []
    p = permutations([1,2,3,4,5,6,7,8,9],3)
    for i in p:
        if sum(i) == 15:
            n.append(list(i))

    n = permutations(n,3)
    for i in n:
        if (i[0][0]+i[1][1]+i[2][2])==15 and (i[0][0]+i[1][0]+i[2][0])==15 and (i[0][1]+i[1][1]+i[2][1])==15 and (i[0][1]+i[1][1]+i[2][1])==15 and (i[1][1] == 5) and (i[0][0]%2==0 and i[0][2]%2==0 and i[2][0]%2==0 and i[2][2]%2==0):
            d.append(list(i))

    for t in d:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost = cost + int(abs(s[i][j] - t[i][j]))
        if minimum_cost is None or cost < minimum_cost:
            minimum_cost = cost
    return minimum_cost


if __name__=='__main__':
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(result)
