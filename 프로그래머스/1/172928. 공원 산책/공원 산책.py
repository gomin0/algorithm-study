def solution(park, routes):
    max_x = len(park[0])
    max_y = len(park)
    x = 0
    y = 0
    
    for find_y in range(max_y):
        for find_x in range(max_x):
            if park[find_y][find_x] == "S":
                x = find_x
                y = find_y
                break
    
    for i in routes:
        a, b = i.split(" ")
        possible = True
        
        if a == "E":
            if x + int(b) < max_x:
                for i in range(1, int(b) + 1):
                    if (park[y][x + i]) == "X":
                        possible = False
                        break
                if possible:
                    x += int(b)
        elif a == "W":
            if x - int(b) >= 0:
                for i in range(1, int(b) + 1):
                    if (park[y][x - i]) == "X":
                        possible = False
                        break
                if possible:
                    x -= int(b)
        elif a == "N":
            if y - int(b) >= 0:
                for i in range(1, int(b) + 1):
                    if (park[y - i][x]) == "X":
                        possible = False
                        break
                if possible:
                    y -= int(b)
        else:  # a == "S"
            if y + int(b) < max_y:
                for i in range(1, int(b) + 1):
                    if (park[y + i][x]) == "X":
                        possible = False
                        break
                if possible:
                    y += int(b)
    
    return [y, x]