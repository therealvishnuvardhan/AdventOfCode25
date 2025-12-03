with open("day3\\input.txt","r") as file:
    content = file.read()
lines = content.split()

result = 0
for line in lines:
    max = 0
    for number1 in range(0,len(line)):
        for number2 in range(number1+1,len(line)):
            final = int(line[number1] + line[number2])
            if final > max:
                max = final
    result = result + max
print(result)



