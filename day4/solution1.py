with open("day4\\input.txt") as file:
    content = file.read()
grid = [list(line) for line in content.split("\n")]

coordinates = [(-1,-1),(-1,0),(-1,1),(0,-1),(1,1),(1,0),(1,-1),(0,1)]

h = len(grid)
w = len(grid[0])

count = 0

for x in range(h):
    for y in range(w):
        if grid[x][y] != "@":
            continue
        adj = 0 
        for dx,dy in coordinates:
            nx , ny = x + dx ,y + dy
            if 0<=nx<h and 0<=ny<w and grid[nx][ny] == "@":
                adj = adj + 1
        if adj < 4:
            count = count + 1
print(count)
        