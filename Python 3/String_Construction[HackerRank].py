
def stringConstruction(s):
    p = ""
    cost = 0
    for i in s:
        if i not in p:
            p = p + i
            cost += 1
    return cost

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()
        result = stringConstruction(s)
        print(result)
