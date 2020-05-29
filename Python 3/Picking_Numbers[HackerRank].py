from collections import Counter

def pickingNumbers(a):
    new_dict = Counter(a)
    a = list(set(a))
    a.sort()
    max_count = 0
    if len(a) == 1:
        return new_dict[a[0]]

    for i in range(len(a)-1):
        if abs(a[i]-a[i+1]) == 1:
            new_count = new_dict[a[i]]+new_dict[a[i+1]]
            if new_count > max_count:
                max_count = new_count

        if new_dict[a[i]] > max_count:
            max_count = new_dict[a[i]]

        if new_dict[a[i+1]] > max_count:
            max_count = new_dict[a[i]]        

    return max_count

if __name__ == '__main__':

    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    print(result)
