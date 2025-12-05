with open ("day5\\input.txt") as file:
    content = file.read()
lines = content.split()

ranges = []
ids = []

for line in lines:
    if "-" in line:
        ranges.append(line)
    else:
        ids.append(int(line))

result = 0
for id in ids:
    valid = False
    for range in ranges:
        start , end = range.split("-")
        if int(start) <= id <= int(end):
            valid = True
    if valid:
        result+=1
print(result)
        




