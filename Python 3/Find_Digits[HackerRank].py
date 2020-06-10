
def findDigits(n):
    count = 0
    temp_1 = n
    while n!=0:
        temp = n%10
        if temp!=0 and temp_1%temp==0:
            count +=1
        n = n//10
    return count

if __name__ == '__main__':

    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = findDigits(n)
        print(result)
