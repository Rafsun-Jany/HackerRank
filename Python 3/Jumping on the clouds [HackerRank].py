def jumpingOnClouds(c):
    n = 0
    jump_count = 0
    while n + 1 < len(c) - 1:
        if c[n + 2] == 0:
            n = n + 2
            jump_count += 1
        elif c[n + 1] == 0:
            n = n + 1
            jump_count += 1

    if n == len(c) - 1:
        return jump_count
    else:
        return jump_count + 1


elements = int(input())
c = list(map(int, input().rstrip().split()))
result = jumpingOnClouds(c)
print(result)
