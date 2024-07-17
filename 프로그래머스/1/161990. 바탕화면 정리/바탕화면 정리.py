def solution(wallpaper):
    
    min_x = 50
    min_y = 50
    max_x = 0
    max_y = 0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                min_x = min(min_x, i)
                min_y = min(min_y, j)
                max_x = max(max_x, i + 1)
                max_y = max(max_y, j + 1)
                
    return [min_x, min_y, max_x, max_y]