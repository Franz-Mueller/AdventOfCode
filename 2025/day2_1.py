lines = open("2025/input.txt").read().split(",")

result = 0

for i in lines:
    low, high = i.split("-")
    for j in range(int(low), int(high) + 1):
        if str(j)[int((len(str(j)) / 2)) :] == str(j)[: int((len(str(j)) / 2))]:
            result += int(j)

print(result)
