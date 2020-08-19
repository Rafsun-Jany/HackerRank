n = int(input())
d = dict()
for i in range(n):
    word = input()

    if word in d.keys():
        d[word] += 1
    else:
        d[word] = 1
print(len(d))

occ = ""

for i in d.values():
    occ = occ + str(i) + " "

print(occ)
