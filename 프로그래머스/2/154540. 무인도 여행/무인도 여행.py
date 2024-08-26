def solution(maps):
    
    def dfs(x, y):
        stack = [(x, y)]
        days = 0
        
        while stack:
            cx, cy = stack.pop()
            
            if visited[cx][cy]:
                continue
            
            visited[cx][cy] = True
            days += int(maps[cx][cy])
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and maps[nx][ny] != 'X':
                    stack.append((nx, ny))
                    
        return days
    
    answer = []
    
    r, c = len(maps), len(maps[0])
    visited = [[False]*c for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(dfs(i, j))
    
    if not answer:
        return [-1]
    
    answer.sort()
    
    return answer