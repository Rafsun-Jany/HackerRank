'''My solution though not passes 5 test cases out off 22'''


def checkMagazine(magazine, note):
    magazine_dict = {}
    k = 0
    for i in magazine:
        magazine_dict[i] = k
        k += 1

    for i in note:
        if i in magazine_dict:
            del magazine_dict[i]
        else:
            print('No')
            return
    print('Yes')


if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    magazine = input().strip().split()
    note = input().strip().split()
    checkMagazine(magazine, note)
