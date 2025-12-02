with open("day2\\input.txt","r") as file:
    content = file.read()
lines = content.split(",")
ranges = []
for line in lines:
   start , end =  line.split("-")
   ranges.append((int(start),int(end)))
print(ranges)

def is_invalid(n):
    s = str(n)
    l = len(s)
    for k in range(1,(l//2)+1):
        if l % k != 0:
            continue
        var = s[:k]
        times = l//k
        if times>=2 and var*times == s:
            return True
    return False
    
count = 0    
for start,end in ranges:
    for number in range(start , end+1):
        if is_invalid(number):
            count = number + count
print(count)

