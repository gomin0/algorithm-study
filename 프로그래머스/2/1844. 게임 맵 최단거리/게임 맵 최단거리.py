def solution(maps):
    answer = 0
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    queue = [(0, 0, 1)]
    
    while queue:
        x, y, dist = queue.pop(0)
        if x == n-1 and y == m - 1:
                return dist
            
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            
            if 0 <= mx < n and 0 <= my < m and not visited[mx][my]:
                if maps[mx][my] == 1:
                    visited[mx][my] = True
                    queue.append((mx, my, dist + 1))
    
    return -1