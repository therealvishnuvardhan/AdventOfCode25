with open("day7\\input.txt") as file:
    content = file.read()
lines = content.splitlines()

input = []

for line in lines:
    list = []
    for char in line:
        list.append(char)
    input.append(list)

for i in range(len(input[0])):
    if input[0][i] == "S":
        x , y = 0 , i

n = len(input)
m = len(input[0])

beams = set()
beams.add(y)
depth = 1
result = 0

while depth != n-1:
    for j in range(m):
        if input[depth][j] == "^" and j in beams:
            beams.remove(j)
            beams.add(j-1)
            beams.add(j+1)
            result += 1
    depth += 1
print(result)





    

        

    
        


        
        
    
    