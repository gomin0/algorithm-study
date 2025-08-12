from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    rectangles = [[x1*2, y1*2, x2*2, y2*2] for x1, y1, x2, y2 in rectangle]
    board = [[0]*102 for _ in range(102)] # 크기가 50까진데 2배 + 여유 공간 2
    
    for x1, y1, x2, y2 in rectangles:
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if x == x1 or x == x2 or y == y1 or y == y2:
                    board[x][y] = 1
    
    for x1, y1, x2, y2 in rectangles:
        for x in range(x1+1, x2):
            for y in range(y1+1, y2):
                board[x][y] = 0
    
    q = deque()
    q.append((characterX * 2, characterY * 2, 0))
    visited = [[False] * 102 for _ in range(102)]
    visited[characterX*2][characterY*2] = True
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while q:
        x, y, d = q.popleft()
        if (x, y) == (itemX * 2, itemY * 2):
            return d // 2
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 102 and 0 <= ny < 102 and not visited[nx][ny]:
                if board[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny, d + 1))