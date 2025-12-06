with open("day6\\input.txt") as file:
    content = file.read()
lines = content.splitlines()

input = []
for line in lines:
    temp = line.split()
    input.append(temp)

total = 0

for i in range(len(input)-1):
    for j in range(len(input[i])):
        input[i][j] = int(input[i][j])


for i in range(len(input[3])):
    if input[4][i] == "*":
        total += input[0][i] * input[1][i] * input[2][i] * input[3][i]

    else:
        total += input[0][i] + input[1][i] + input[2][i] + input[3][i]
print(total)
