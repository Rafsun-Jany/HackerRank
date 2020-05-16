def countApplesAndOranges(s, t, a, b, apples, oranges):

    p = [a+i for i in apples]
    q = [b+i for i in oranges]
    p = [i for i in p if s<=i<=t]
    q = [i for i in q if s<=i<=t]
    print(len(p))
    print(len(q))

if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
