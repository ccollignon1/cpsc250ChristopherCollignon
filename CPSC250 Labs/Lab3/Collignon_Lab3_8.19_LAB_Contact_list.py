list1 = input().split(' ')
for x in range(len(list1)):
    list1[x] = list1[x].split(',')
name = input()
c1 = 0
c2 = 0
for x in list1:
    c1 += 1
    c2 = 0
    for y in range(len(x)):
        c2 += 1
        if x[y] == name:
            c1_keep = c1 - 1
            c2_keep = c2
print(list1[c1_keep][c2_keep])

