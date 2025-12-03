input = open("2025/input.txt").read().splitlines()

count = 0

for i in input:
    highest = 0
    p1 = 0
    p2 = 1
    while p2 < len(i):
        if p1 >= p2:
            p2 += 1
            p1 = 0
            continue
        if int(str(i[p1]) + str(i[p2])) > highest:
            highest = int(str(i[p1]) + str(i[p2]))
        p1 += 1
    count += highest

print(count)
