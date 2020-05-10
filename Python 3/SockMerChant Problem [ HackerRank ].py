def sockMerchant(n, ar):
    count_pairs = 0
    ar_new = set(ar)
    for i in ar_new:
        count = ar.count(i)
        count_pairs = count_pairs + count // 2

    return count_pairs


if __name__ == '__main__':
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)
