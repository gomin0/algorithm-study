from collections import deque

def bfs(maps, start, end):
    
    rows = len(maps)
    cols = len(maps[0])
    
    queue = deque([(start, 0)]) # (start, 거리)
    visited = [[False] * cols for _ in range(rows)]
    visited[start[0]][start[1]] = True

    while queue:
        (x, y), distance = queue.popleft()
        
        if (x, y) == end:
            return distance
        
        for dx, dy in[(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maps[nx][ny] != 'X' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append(((nx, ny), distance + 1))
    return -1

def solution(maps):
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                exit = (i, j)
    
    to_lever = bfs(maps, start, lever)
    if to_lever == -1:
        return -1
    
    to_exit = bfs(maps, lever, exit)
    if to_exit == -1:
        return -1
    
    return to_lever + to_exit