from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    oil_dict = [0] * m
    
    visited = [[False] * m for _ in range(n)]
    
    def bfs(x, y):
        count = 1
        q = deque([(x, y)])
        visited[x][y] = True
        oil_columns = set([y])
        
        while q:
            cx, cy = q.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    count += 1
                    oil_columns.add(ny)
        return count, oil_columns
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                c, o = bfs(i, j)
                for col in o:
                    oil_dict[col] += c
                            
    max_oil = max(oil_dict) if oil_dict else 0
    
    return max_oil