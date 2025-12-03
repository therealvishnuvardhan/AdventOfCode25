with open("day3\\input.txt","r") as file:
    content = file.read()
lines = content.split()

final = 0

for line in lines:
    result = []

    const = 12
    var = const
    start = 0
    while var > 0:
        
        end = len(line) - var+1
        window = line[start : end]
        best_num = max(window)
        best_index = window.index(best_num)
        result.append(best_num)
        start += best_index + 1
        var -= 1
    final += int("".join(result))
        
print(final)

        




    



    