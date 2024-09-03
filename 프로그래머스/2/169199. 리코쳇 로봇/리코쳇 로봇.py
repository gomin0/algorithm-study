from collections import deque

def solution(board):
    answer = 0
    
    start_x, start_y = 0, 0
    
    n, m = len(board), len(board[0])
    
    start = False
    for a in range(n):
        if start:
            break
        for b in range(m):
            if board[a][b] == 'R':
                start_x, start_y = a, b
                start = True
                break
    
    queue = deque([(start_x, start_y, 0)]) # 좌표, 이동 횟수
    visited = set()
    visited.add((start_x, start_y))
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y, moves = queue.popleft()
        
        if board[x][y] == 'G':
            return moves
        
        for dx, dy in directions:
            nx, ny = x, y
            
            while 0 <= nx + dx < n and 0 <= ny + dy < m and board[nx + dx][ny + dy] != 'D':
                nx += dx
                ny += dy
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, moves + 1))
                
    return -1