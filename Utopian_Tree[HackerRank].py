def utopianTree(n):
    tree_height = 1
    total_height = 0
    if n == 0:
        return 1
    else:
        for i in range(1,n+1):
            if i%2==0:
                total_height += 1
                tree_height = total_height
            else:
                total_height = (tree_height*2)
                tree_height = total_height
    return total_height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
