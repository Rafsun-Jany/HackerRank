# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    max_amount = 0
    if min(keyboards) + min(drives) > b:
        return -1
    else:
        for i in keyboards:
            for j in drives:
                if i+j <= b:
                    if i+j > max_amount:
                        max_amount = i+j
    return max_amount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
