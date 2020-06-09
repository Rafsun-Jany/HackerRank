
# Complete the permutationEquation function below.
def permutationEquation(p):
    for i in range(1,len(p)+1):
        if i in p:
            temp = p.index(i)
            temp = temp + 1
            temp = p.index(temp)
            temp = temp + 1
            print(temp)

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().rstrip().split()))
    result = permutationEquation(p)
