import math

with open("day8\\input.txt") as file:
    content = file.read()
lines = content.split()

coordinates = []
for line in lines:
    x , y ,z = line.split(",")
    coordinates.append((int(x) , int(y) , int(z)))

pairs = []
n = len(coordinates)
for i in range(n):
    for j in range(i+1,n):
        x1,y1,z1 = coordinates[i]
        x2,y2,z2 = coordinates[j]
        dist = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
        pairs.append((dist , i , j))
pairs.sort()

circuits = [[i] for i in range(n)]

def check_groups(point):
    
    for idx, group in enumerate(circuits):
        if point in group:
            return idx
    return None

count = 0 
for dist , i , j in pairs:
    if count == 1000:
        break

    group1 = check_groups(i)
    group2 = check_groups(j)

    if group1 is None or group2 is None:
        count = count + 1
        continue

    if group1 != group2:
        
        if group1 < group2:
            circuits[group1].extend(circuits[group2])
            del circuits[group2]
        else:
            circuits[group2].extend(circuits[group1])
            del circuits[group1]
    count = count + 1

final = []
for group in circuits:
    final.append(len(group))
final.sort(reverse=True)

if len(final) >= 3:
    result = final[0] * final[1] * final[2]
else:
    result = 1
    for s in final:
        result *= s

print(result)
