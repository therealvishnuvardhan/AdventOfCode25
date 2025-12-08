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

for dist, i, j in pairs:
   
    group1 = check_groups(i)
    group2 = check_groups(j)

    if group1 is None or group2 is None:
        continue

    if group1 != group2:
       
        if group1 < group2:
            circuits[group1].extend(circuits[group2])
            del circuits[group2]
        else:
            circuits[group2].extend(circuits[group1])
            del circuits[group1]

        if len(circuits) == 1:
            x1 = coordinates[i][0]
            x2 = coordinates[j][0]
            product = x1 * x2
            print( product)
            break
