
def cutTheSticks(arr):
    sticks_cut = []
    while len(arr) != 0:
        sticks_cut.append(len(arr))
        shortest_piece = min(arr)
        arr = [i for i in arr if i-shortest_piece !=0]

    for i in sticks_cut:
        print(i)

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)
