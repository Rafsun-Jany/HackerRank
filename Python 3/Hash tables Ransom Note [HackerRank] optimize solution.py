from collections import Counter


def checkMagazine(magazine, note):
    return Counter(note) - Counter(magazine)


if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    magazine = input().strip().split()
    note = input().strip().split()
    checkMagazine(magazine, note)
    if checkMagazine():
        print('Yes')
    else:
        print('No')
