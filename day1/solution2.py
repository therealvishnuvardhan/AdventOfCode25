count = 0
pos = 50
with open("day1\\input.txt","r") as file:
    content = file.read()
    lines = content.split("\n")
for line in lines:
    dir = line[0]
    val = int(line[1:])

    i = 0
    while i < val:
        if dir == "R":
            pos = (pos + 1) % 100
        else:
            pos = (pos -1) % 100
        
    
        if pos == 0:
            count = count + 1
        i = i + 1

print(count)