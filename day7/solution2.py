with open("day7\\input.txt") as file:
    content = file.read()
lines = content.splitlines()

input = []
for line in lines:
    row = []
    for char in line:
        row.append(char)
    input.append(row)

for i in range(len(input[0])):
    if input[0][i] == "S":
        x, y = 0, i
        break

n = len(input)
m = len(input[0])

startX = x + 1
startY = y

active = { str(startX) + "," + str(startY) : 1 }
result = 0

while active:
    next_map = {}

    for key, count in active.items():
        parts = key.split(",")
        cx = int(parts[0])
        cy = int(parts[1])

        if cx < 0 or cx >= n or cy < 0 or cy >= m:
            result += count
            continue

        cell = input[cx][cy]

        if cell == '^':
            left = cy - 1
            if left >= 0:
                k = str(cx) + "," + str(left)
                next_map[k] = next_map.get(k, 0) + count
            else:
                result += count

            right = cy + 1
            if right < m:
                k = str(cx) + "," + str(right)
                next_map[k] = next_map.get(k, 0) + count
            else:
                result += count

        else:
            nx = cx + 1
            if nx < n:
                k = str(nx) + "," + str(cy)
                next_map[k] = next_map.get(k, 0) + count
            else:
                result += count

    active = next_map

print("result:", result)
