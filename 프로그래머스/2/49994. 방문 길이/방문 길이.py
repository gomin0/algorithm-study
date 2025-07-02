def solution(dirs):
    x: int = 0
    y: int = 0
    max_x: int = 5
    max_y: int = 5
    min_y: int = -5
    min_x: int = -5
    path: set[tuple[int, int, int, int]] = set()
    
    for d in dirs:
        dx: int = 0
        dy: int = 0
        if d == "U":
            dy = 1
        elif d == "D":
            dy = -1
        elif d == "R":
            dx = 1
        else:
            dx = -1
        nx: int = x + dx
        ny: int = y + dy
        if min_x <= nx <= max_x and min_y <= ny <= max_y:
            path.add((x, y, nx, ny))
            path.add((nx, ny, x, y))
            x = nx
            y = ny
    
    answer: int = len(path) // 2
    return answer