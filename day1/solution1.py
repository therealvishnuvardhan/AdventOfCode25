count = 0
pos = 50
with open("day1\\input.txt","r") as file:
    content = file.read()
    lines = content.split("\n")
for line in lines:
    dir = line[0]
    val = int(line[1:])

    if dir == "R":
        pos = pos + val
    else:
        pos = pos - val

    pos = pos % 100

    if pos == 0:
        count = count + 1

print(count)