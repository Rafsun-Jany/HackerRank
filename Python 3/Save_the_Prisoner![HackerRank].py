# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    temp = ((m%n)-1+s)%n

    return n if temp ==0 else temp

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nms = input().split()
        n = int(nms[0])
        m = int(nms[1])
        s = int(nms[2])
        result = saveThePrisoner(n, m, s)
        print(result)
