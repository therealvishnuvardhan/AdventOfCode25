with open("day2\\input.txt","r") as file:
    content = file.read()
lines = content.split(",")
ranges = []
for line in lines:
   start , end =  line.split("-")
   ranges.append((int(start),int(end)))
print(ranges)

def is_invalid(n):
    num_string = str(n)
    if len(num_string) % 2 != 0:
        return False
    else:
        mid = len(num_string)//2
        return num_string[:mid] == num_string[mid:]
    
count = 0    
for start,end in ranges:
    for number in range(start , end+1):
        if is_invalid(number):
            count = number + count
print(count)

            


    





