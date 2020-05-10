def minimumSwaps(arr):
    count = 0
    dict_arr = {j:i for i,j in enumerate(arr)}
    sorted_arr = sorted(arr)

    for i in range(len(arr)):
        replace_value = sorted_arr[i]
        swap_index = dict_arr[replace_value]

        if arr[i] != sorted_arr[i]:
            arr[i],arr[swap_index] = arr[swap_index],arr[i]
            dict_arr[replace_value] = i
            dict_arr[arr[swap_index]] = swap_index
            count +=1

    return count



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    print(res)
