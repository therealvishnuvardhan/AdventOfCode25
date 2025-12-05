with open ("day5\\input.txt") as file:
    content = file.read()
lines = content.split()

ranges = []

for line in lines:
    if "-" in line:
        start , end = line.split("-")
        ranges.append((int(start),int(end)))
ranges.sort()

merged = []
cs , ce = ranges[0]
for start , end in ranges[1:]:
    if start <= ce + 1:
        ce = max(end , ce)
    else:
        merged.append((cs,ce))
        cs , ce = start , end
merged.append((cs,ce))

count = 0
for start , end in merged:
    count += len(range(start , end+1))
print(count)





        



