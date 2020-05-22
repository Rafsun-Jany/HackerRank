
def birthday(s, d, m):
    count = 0
    segment = [s[i:i+m] for i in range(len(s)) if i+1<len(s) or len(s)==1]
    for i in segment:
        if sum(i) == d:
            count +=1
    return count

if __name__ == '__main__':

    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    dm = input().rstrip().split()
    d = int(dm[0])
    m = int(dm[1])
    result = birthday(s, d, m)
    print(result)
