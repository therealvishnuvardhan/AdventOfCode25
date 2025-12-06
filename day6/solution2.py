with open("day6\\input.txt") as file:
    content = file.read()
lines = content.splitlines()

n = len(lines[0])
nums = []
result = 0

for i in range(n-1, -1, -1):

    op = lines[4][i]

    currnum = lines[0][i] + lines[1][i] + lines[2][i] + lines[3][i]
    currnum = currnum.strip()                    

    if currnum != "":                            
        nums.append(int(currnum))               

    if op == "+" or op == "*":

        if op == "+":                            
            temp = 0                             
            for num in nums:
                temp += num
            result += temp                       

        else:
            temp = 1                             
            for num in nums:
                temp *= num
            result += temp                      
        nums.clear()                             

print(result)
