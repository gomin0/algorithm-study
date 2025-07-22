import sys
from collections import deque
sys.setrecursionlimit(10000)

def solution(n, m, x, y, r, c, k):
    directions: list[str] = ['d', 'l', 'r', 'u']
    dx: list[int] = [1, 0, 0, -1]
    dy: list[int] = [0, -1, 1, 0]
    
    dist: int = abs(x-r) + abs(y-c)
    if dist > k or (k-dist) % 2 != 0:
        return "impossible"
    
    answer = None
    found = False
    def dfs(cx, cy, path, steps):
        nonlocal answer, found
        if found:
            return
        if steps == k:
            if cx == r and cy == c:
                answer = path
                found = True
            return
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 1 <= nx <= n and 1 <= ny <= m:
                remain = abs(nx - r) + abs(ny - c)
                if remain > k - steps - 1:
                    continue
                if (k - steps - 1 - remain) % 2 != 0:
                    continue
                dfs(nx, ny, path + directions[i], steps + 1)
    
    dfs(x, y, "", 0)
    
    return answer if answer else "impossible"