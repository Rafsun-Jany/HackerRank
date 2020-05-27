

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    bill.remove(bill[k])
    bill = sum(bill)
    bill = bill/2
    if bill == b:
        print('Bon Appetit')
    else:
        print(int(b-bill))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
