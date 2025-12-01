lines = open("2025/input.txt").read().splitlines()

pos = 50

count = 0

for i in lines:
    move_by = int(i[1:])
    if move_by >= 100:
        count += int(move_by / 100)
        move_by = move_by % 100

    if i.startswith("L"):
        substracted = pos - move_by
        if substracted < 0:
            if pos != 0:
                count += 1
            pos = 100 - (move_by - pos)
        else:
            pos = substracted
    elif i.startswith("R"):
        added_up = pos + move_by
        if added_up > 99:
            if added_up != 100:
                count += 1
            pos = 0 + (pos + move_by - 100)
        else:
            pos = added_up

    if pos == 0:
        count += 1

    print(f"The dial is rotated {i} to point at {pos}")

print(count)
