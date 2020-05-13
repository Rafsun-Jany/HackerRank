def staircase(n):
    for i in range(1, n + 1):
        symbol = int(i) * '#'
        print(symbol.rjust(n))


if __name__ == '__main__':
    n = int(input())

    staircase(n)
