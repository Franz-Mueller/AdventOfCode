input = open("2025/input.txt").read().splitlines()

count = 0

for i in input:
    p1 = 0
    index = -1
    lower_limit = 0
    number = ""
    for j in range(12, 0, -1):
        highest = 0
        p1 = index + 1
        while p1 < len(i) - (j - 1):
            if int(i[p1]) > highest:
                highest = int(i[p1])
                index = p1
            p1 += 1
        number += i[index]
    count += int(number)

print(count)
