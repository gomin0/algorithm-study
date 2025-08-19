from collections import deque

def solution(board):
    visited = set()
    n: int = len(board)
    q = deque([(0, 0, 0, 1, 0)])
    visited.add((0, 0, 0, 1))
    visited.add((0, 1, 0, 0))
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        sx1, sy1, sx2, sy2, d = q.popleft()
        if (sx1 == n-1 and sy1 == n-1) or (sx2 == n-1 and sy2 == n-1):
            return d
        # 상하좌우 이동
        for i in range(4):
            nx1 = sx1 + direction[i][0]
            ny1 = sy1 + direction[i][1]
            nx2 = sx2 + direction[i][0]
            ny2 = sy2 + direction[i][1]
            
            if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n and board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
                if (nx1, ny1, nx2, ny2) not in visited:
                    visited.add((nx1, ny1, nx2, ny2))
                    visited.add((nx2, ny2, nx1, ny1))
                    q.append((nx1, ny1, nx2, ny2, d+1))
        # 회전 이동
        if sx1 == sx2:
            for dd in [-1, 1]:
                if 0 <= sx1+dd < n and 0 <= sx2+dd < n:
                    if board[sx1+dd][sy1] == 0 and board[sx2+dd][sy2] == 0:
                        if (sx1, sy1, sx1+dd, sy1) not in visited:
                            visited.add((sx1, sy1, sx1+dd, sy1))
                            visited.add((sx1+dd, sy1, sx1, sy1))
                            q.append((sx1, sy1, sx1+dd, sy1, d+1))
                        if (sx2, sy2, sx2+dd, sy2) not in visited:
                            visited.add((sx2, sy2, sx2+dd, sy2))
                            visited.add((sx2+dd, sy2, sx2, sy2))
                            q.append((sx2, sy2, sx2+dd, sy2, d+1))
        elif sy1 == sy2:
            for dd in [-1, 1]:
                if 0 <= sy1+dd < n and 0 <= sy2+dd < n:
                    if board[sx1][sy1+dd] == 0 and board[sx2][sy2+dd] == 0:
                        if (sx1, sy1, sx1, sy1+dd) not in visited:
                            visited.add((sx1, sy1, sx1, sy1+dd))
                            visited.add((sx1, sy1+dd, sx1, sy1))
                            q.append((sx1, sy1, sx1, sy1+dd, d+1))
                        if (sx2, sy2, sx2, sy2+dd) not in visited:
                            visited.add((sx2, sy2, sx2, sy2+dd))
                            visited.add((sx2, sy2+dd, sx2, sy2))
                            q.append((sx2, sy2, sx2, sy2+dd, d+1))
    
    return -1

