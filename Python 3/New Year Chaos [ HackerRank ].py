def minimumBribes(aim_list):
    initial_list = [i for i in range(1, len(q) + 1)]
    number_of_bribes = 0
    for i in range(len(q)):
        for j in range(i, len(q)):
            if aim_list[i] == initial_list[j]:
                break
            else:
                if initial_list[j + 1] == aim_list[i]:
                    initial_list[j], initial_list[j + 1] = initial_list[j + 1], initial_list[j]
                    number_of_bribes += 1
                    break
                elif initial_list[j + 2] == aim_list[i]:
                    p = 2
                    for _ in range(p):
                        second_itr = j + p
                        initial_list[second_itr - 1], initial_list[second_itr] = initial_list[second_itr], initial_list[
                            second_itr - 1],
                        p = p - 1
                        number_of_bribes += 1
                    break
                else:
                    print('Too chaotic')
                    return

    print(number_of_bribes)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
