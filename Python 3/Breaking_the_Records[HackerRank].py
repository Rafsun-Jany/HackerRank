def breakingRecords(scores):
    min_count = max_count = 0
    min_value = scores[0]
    max_value = scores[0]
    for i in scores:
        if i > max_value:
            max_count +=1
            max_value = i
        elif i < min_value:
            min_value = i
            min_count +=1
    return max_count,min_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
